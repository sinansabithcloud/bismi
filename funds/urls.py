from django.urls import path
from .views import FundListView, FundDetailView, transfer_funds, ExpenseCreateView, FundUpdateView, ExpenseUpdateView, ExpenseListView, ExpenseTypeCreateView

urlpatterns = [
    path('', FundListView.as_view(), name='list_funds'),
    path('<int:pk>/', FundDetailView.as_view(), name='view_fund'),
    path('<int:pk>/edit/', FundUpdateView.as_view(), name='edit_fund'),

    path('transfer/', transfer_funds, name='transfer_funds'),

    path('expenses/', ExpenseListView.as_view(), name='list_expense'),
    path('expenses/create/', ExpenseCreateView.as_view(), name='create_expense'),
    path('expenses/<int:pk>/edit/', ExpenseUpdateView.as_view(), name='edit_expense'),
    
    path('expenses/type/', ExpenseTypeCreateView.as_view(), name='create_expense_type'),
]
