from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Transaction, Budget

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'type', 'category', 'description', 'date']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',  # HTML5 date picker
                    'value': timezone.now().strftime('%Y-%m-%d')  # Today by default
                }
            ),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Описание транзакции...'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0.01', 'placeholder': '0.00'}),
            'type': forms.Select(attrs={'id': 'id_type'}),
            'category': forms.Select(attrs={'id': 'id_category'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise ValidationError('Сумма должна быть положительной')
        return amount
    
    def clean_date(self):
        date = self.cleaned_data['date']
        if date.date() > timezone.now().date():
            raise ValidationError('Дата не может быть в будущем')
        return date
    
    def clean(self):
        cleaned_data = super().clean()
        transaction_type = cleaned_data.get('type')
        category = cleaned_data.get('category')
        
        # Category must correspond to transaction type
        if category and transaction_type:
            if category.type != transaction_type:
                raise ValidationError(
                    f'Категория "{category.name}" не подходит для типа "{transaction_type}"'
                )
        
        return cleaned_data

    # Add CSS classes for stylization 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'period', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'id': 'id_start_date'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date', 
                'id': 'id_end_date'
            }),
            'amount': forms.NumberInput(attrs={
                'step': '0.01', 
                'min': '0.01',
                'placeholder': '0.00'
            }),
        }
        labels = {
            'amount': 'Сумма бюджета',
            'period': 'Период',
            'start_date': 'Начало периода',
            'end_date': 'Конец периода',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise ValidationError('Сумма бюджета должна быть положительной')
        return amount
    
    # FIX: Error hint not showing
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if start_date >= end_date:
                raise ValidationError('Дата окончания должна быть позже даты начала')
        
        return cleaned_data