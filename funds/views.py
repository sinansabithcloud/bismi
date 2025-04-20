from django.shortcuts import render
from .models import Fund, Expense, ExpenseType
from billapp.globalmixins import ModelNameContextMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

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