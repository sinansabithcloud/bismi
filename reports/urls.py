from django.urls import path
from .views import daily_report, monthly_report

urlpatterns = [
    path('', daily_report, name='daily_report'),
    path('monthly/', monthly_report, name='monthly_report'),
]
