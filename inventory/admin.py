from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.StockType)
admin.site.register(models.Stock)
admin.site.register(models.StockSet)