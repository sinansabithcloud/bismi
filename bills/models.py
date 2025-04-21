from django.db import models
from funds.models import Fund

# Create your models here.

class SalesBillType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models

class SalesBill(models.Model):
    bill_datetime = models.DateTimeField(auto_now_add=True)  # keep original for now
    bill_date = models.DateField(auto_now_add=True)
    bill_time = models.TimeField(auto_now_add=True)

    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='salesbills')
    sales_bill_type = models.ForeignKey(SalesBillType, on_delete=models.CASCADE, related_name='salesbills')
    customer = models.CharField(max_length=255, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer}"
    
    @property
    def bill_number(self):
        return f"{self.pk:05d}"
    
    @property
    def stocks(self):
        return {sale.stockset.name: sale.quantity for sale in self.sales.all()}
    
    @property
    def total_amount_before_discount(self):
        return sum(sale.net_total_price for sale in self.sales.all())
    
    @property
    def discount_percent(self):
        if self.total_amount_before_discount > 0:
            return (self.discount_price / self.total_amount_before_discount) * 100
        return 0

    @property
    def total_amount_after_discount(self):
        return self.total_amount_before_discount - self.discount_price
    


    