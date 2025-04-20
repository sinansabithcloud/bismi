from django.shortcuts import render
from django.http import JsonResponse
from .models import Purchase
from billapp.globalmixins import ModelNameContextMixin
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from inventory.models import StockSet

# Create your views here.

def home(request):
    return render(request, 'transactions/home.html')
    
class PurchaseCreateView(ModelNameContextMixin, CreateView):
    model = Purchase
    fields = ['stockset', 'fund', 'quantity', 'price_per_unit', 'return_quantity', 'return_price_per_unit']
    template_name = 'model_create_edit_form.html'
    success_url = reverse_lazy('home')

class PurchaseUpdateView(ModelNameContextMixin, UpdateView):
    model = Purchase
    fields = ['stockset', 'fund', 'quantity', 'price_per_unit', 'return_quantity', 'return_price_per_unit']
    template_name = 'model_create_edit_form.html'
    success_url = reverse_lazy('home')

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'transactions/purchases_history.html'
    ordering = ['-date']

from django.http import JsonResponse

def get_stock_cost(request):
    stockset_id = request.GET.get('stockset_id')
    stockset = StockSet.objects.filter(id=stockset_id).first()
    if stockset:
        cost_price = stockset.cost_price
        return JsonResponse({
            'cost_price': cost_price
        })
    return JsonResponse({
        'cost_price': 0
    })
