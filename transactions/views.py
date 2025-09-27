from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
# from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .models import Transaction, Budget
from .forms import TransactionForm, BudgetForm
import json

def custom_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto login after registration
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    
    def get_queryset(self):
       return Transaction.objects.filter(user=self.request.user).order_by('-date')

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = '/transactions/'
    
    def form_valid(self, form):
        # Bind transaction to current user
        form.instance.user = self.request.user
        messages.success(self.request, 'Транзакция успешно добавлена!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Пожалуйста, исправьте ошибки в форме.')
        return super().form_invalid(form)
    
class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'transactions/budget_form.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Бюджет успешно установлен!')
        return super().form_valid(form)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    income_total = Transaction.objects.filter(
        type='income', 
        user=request.user
    ).aggregate(Sum('amount'))['amount__sum'] or 0
    
    expense_total = Transaction.objects.filter(
        type='expense', 
        user=request.user
    ).aggregate(Sum('amount'))['amount__sum'] or 0
    
    balance = income_total - expense_total

    # Object of type Decimal is not JSON serializable
    # So convert to float
    income_total = float(income_total)
    expense_total = float(expense_total)
    balance = float(balance)
    
    thirty_days_ago = timezone.now() - timedelta(days=30)
    
    category_stats = Transaction.objects.filter(
        type='expense',
        user=request.user,
        date__gte=thirty_days_ago
    ).values('category__name').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')

     # Convert Decimal to float for category_stats
    category_stats_list = []
    for stat in category_stats:
        category_stats_list.append({
            'category__name': stat['category__name'],
            'total': float(stat['total'] or 0),
            'count': stat['count']
        })
    
    # Budget comparison
    current_budgets = Budget.objects.filter(
        user=request.user,
        start_date__lte=timezone.now().date(),
        end_date__gte=timezone.now().date()
    )
    
    budget_comparison = []
    for budget in current_budgets:
        actual_spent = Transaction.objects.filter(
            user=request.user,
            category=budget.category,
            type='expense',
            date__range=[budget.start_date, budget.end_date]
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        budget_comparison.append({
            'category': budget.category.name,
            'budget_amount': float(budget.amount),  # Convert for JSON
            'actual_spent': float(actual_spent),    # Convert for JSON
            'remaining': float(budget.amount - actual_spent),
        })
    
    # Convert QuerySet to JSON list
    category_stats_list = list(category_stats)
    
    context = {
        'balance': balance,
        'income_total': income_total,
        'expense_total': expense_total,
        'category_stats': category_stats_list,
        'category_stats_json': json.dumps(category_stats_list, default=str),  # JSON for JavaScript
        'budget_comparison': budget_comparison,
        'budget_comparison_json': json.dumps(budget_comparison, default=str),  # JSON for JavaScript
    }
    return render(request, 'transactions/dashboard.html', context)

def index(request):
    return render(request, 'transactions/index.html')