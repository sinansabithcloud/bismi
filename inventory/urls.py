# urls.py
from django.urls import path
from .views import *

urlpatterns = [

    path('', Inventory.as_view(), name='inventory'),

    # Create
    path('stock/create/', StockCreateView.as_view(), name='create_stock_view'),
    path('stockset/create/', StockSetCreateView.as_view(), name='create_stockset_view'),
    path('stocktypes/create/', StockTypeCreateView.as_view(), name='create_stocktype_view'),

    # Edit
    path('stock/<int:pk>/edit/', StockUpdateView.as_view(), name='edit_stock_view'),
    path('stockset/<int:pk>/edit/', StockSetUpdateView.as_view(), name='edit_stockset_view'),
    path('stocktypes/<int:pk>/edit/', StockTypeUpdateView.as_view(), name='edit_stocktype_view'),

    # View
    path('stocktypes/<int:pk>/', StockTypeDetailView.as_view(), name='stocktype_detail'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('stocksets/<int:pk>/', StockSetDetailView.as_view(), name='stockset_detail'),

    #api
    path('api/get_stock_details/', get_stock_details, name='get_stock_details'),


]

