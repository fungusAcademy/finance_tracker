from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import TransactionForm

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
        return super().form_valid(form)

def index(request):
    return render(request, 'transactions/index.html')