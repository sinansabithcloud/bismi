from django.urls import path
from .views import home, PurchaseCreateView, PurchaseListView, PurchaseUpdateView, get_stock_cost

urlpatterns = [
    path('', home, name='home'),
    path('purchase/', PurchaseCreateView.as_view(), name='create_purchase_view'),
    path('purchase/history/', PurchaseListView.as_view(), name='list_purchase_view'),
    path('purchase/<int:pk>/', PurchaseUpdateView.as_view(), name='edit_purchase'),

    #api
    path('api/get_stock_cost/', get_stock_cost, name='get_stock_cost'),
]
