from django import forms
from .models import FundTransfer

class FundTransferForm(forms.ModelForm):
    class Meta:
        model = FundTransfer
        fields = ['from_fund', 'to_fund', 'amount', 'notes']
        widgets = {
            'from_fund': forms.Select(attrs={'class': 'form-control'}),
            'to_fund': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
