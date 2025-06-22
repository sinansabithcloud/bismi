from django.urls import path
from . import views

urlpatterns = [
    path('retail/', views.SalesBillCreateView.as_view(), name='create_retail_view'),
    path('wholesale/', views.SalesBillCreateView.as_view(), name='create_wholesale_view'),
    path('<int:pk>/', views.SalesBillUpdateView.as_view(), name='edit_sale'),
    path('delete/<int:pk>/', views.SalesBillDeleteView.as_view(), name='delete_sale_view'),
    path('bills/', views.SalesBillListView.as_view(), name='list_sale_view'),
    path('bill/', views.bills, name='bills'),
    path('<int:bill_number>/thermal', views.thermal_sales_bill, name='thermal_sales_bill'),
    path('<int:bill_number>/full', views.full_sales_bill, name='full_sales_bill'),
    
]
