from django.shortcuts import render, redirect
from .models import Fund, Expense, ExpenseType, FundTransfer
from billapp.globalmixins import ModelNameContextMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib import messages
from decimal import Decimal
from .forms import FundTransferForm

# Create your views here.

class FundListView(ListView):
    model = Fund
    template_name = 'funds/list_funds.html'

class FundUpdateView(ModelNameContextMixin, UpdateView):
    model = Fund
    fields = ['name', 'opening_balance']
    template_name = 'model_create_edit_form.html'
    success_url = reverse_lazy('list_funds')

class FundDetailView(DetailView):
    model = Fund
    template_name = 'funds/detail_fund.html'
    context_object_name = 'fund'

'''
def transfer_funds(request):
    if request.method == 'POST':
        from_id = request.POST.get('from_fund')
        to_id = request.POST.get('to_fund')
        amount = Decimal(request.POST.get('amount', 0))
        notes = request.POST.get('notes', '')

        try:
            from_fund = Fund.objects.get(id=from_id)
            to_fund = Fund.objects.get(id=to_id)

            transfer = FundTransfer(from_fund=from_fund, to_fund=to_fund, amount=amount, notes=notes)
            transfer.save()
            messages.success(request, "Funds transferred successfully.")
        except Exception as e:
            messages.error(request, f"Transfer failed: {str(e)}")

        return redirect('fund-transfer')  # Redirect to your desired page

    funds = Fund.objects.all()
    return render(request, 'funds/transfer_funds.html', {'funds': funds})

'''

def transfer_funds(request):
    if request.method == 'POST':
        form = FundTransferForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Transfer successful.')
                return redirect('list_funds')
            except Exception as e:
                messages.error(request, f'Transfer failed: {e}')
    else:
        form = FundTransferForm()

    return render(request, 'funds/transfer_funds.html', {'form': form})


class ExpenseCreateView(ModelNameContextMixin, CreateView):
    model = Expense
    fields = ['date', 'amount', 'expense_type', 'fund', 'description']
    template_name = 'model_create_edit_form.html'
    success_url = reverse_lazy('create_expense')

class ExpenseListView(ListView):
    model = Expense
    template_name = 'funds/expenses_history.html'
    ordering = ['-date']

class ExpenseUpdateView(ModelNameContextMixin, UpdateView):
    model = Expense
    fields = ['date', 'amount', 'expense_type', 'fund', 'description']
    template_name = 'model_create_edit_form.html'
    success_url = reverse_lazy('create_expense')



class ExpenseTypeCreateView(ModelNameContextMixin, CreateView):
    model = ExpenseType
    fields = ['name']
    template_name = 'model_create_edit_form.html'
    success_url = reverse_lazy('create_expense')