from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Transaction
from .forms import TransactionForm

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    
    def get_queryset(self):
        return Transaction.objects.all().order_by('-date')[:50]  # last 50 transactions

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    
    def form_valid(self, form):
        # Should be real user binding in production
        return super().form_valid(form)

def index(request):
    return render(request, 'transactions/index.html')