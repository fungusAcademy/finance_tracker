from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Transaction, Budget
from .forms import TransactionForm, BudgetForm


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    
    def get_queryset(self):
        # ADD: show transactions only for specific user
        return Transaction.objects.all().order_by('-date')[:50]  # last 50 transactions

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


def index(request):
    return render(request, 'transactions/index.html')