from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', include('transactions.urls')),
    path('inventory/', include('inventory.urls')),
    path('funds/', include('funds.urls')),
    path('sale/', include('bills.urls')),
    path('reports/', include('reports.urls')),
]
