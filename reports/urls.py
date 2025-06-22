from django.urls import path
from .views import daily_report, monthly_report, profit_report, day_book, redirect_to_selected_day_book

urlpatterns = [
    path('', daily_report, name='daily_report'),
    path('monthly/', monthly_report, name='monthly_report'),
    path('profit/', profit_report, name='profit_report'),
    path('daybook/<str:date>/', day_book, name='day_book'),
    path('daybook/', redirect_to_selected_day_book, name='redirect_to_selected_day_book'),
    
]
