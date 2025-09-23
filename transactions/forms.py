from django import forms
from .models import Transaction
from django.utils import timezone

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
            'description': forms.Textarea(attrs={'rows': 3}),
        }