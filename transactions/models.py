from django.db import models
from inventory.models import StockSet
from funds.models import Fund
from django.core.validators import MinValueValidator
from bills.models import SalesBill

# Create your models here.

class Sale(models.Model):
    stockset = models.ForeignKey(StockSet, on_delete=models.CASCADE, related_name='sales')
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    return_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    return_price_per_unit = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    bill = models.ForeignKey(SalesBill, on_delete=models.CASCADE, related_name='sales', null=True, blank=True)

    def __str__(self):
        return f"Sold {self.quantity} units of {self.stockset} at {self.price_per_unit} each"
    
    @property
    def stock_names(self):
        return [stock for stock in self.stockset.stock.all()]

    @property
    def total_price_before_returns(self):
        return self.quantity * self.price_per_unit

    @property
    def return_total_price(self):
        return self.return_quantity * self.return_price_per_unit

    @property
    def net_total_price(self):
        return self.total_price_before_returns - self.return_total_price

    @property
    def net_quantity(self):
        return self.quantity - self.return_quantity
    
    @property
    def profit(self):
        total_cost = self.stockset.cost_price * self.net_quantity
        return self.net_total_price - total_cost
    


class Purchase(models.Model):
    stockset = models.ForeignKey(StockSet, on_delete=models.CASCADE, related_name='purchases')

    datetime = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    return_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    return_price_per_unit = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='purchases')

    def __str__(self):
        return f"Purchased {self.quantity} units of {self.stockset} at {self.price_per_unit} each"

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

    @property
    def return_total_price(self):
        return self.return_quantity * self.return_price_per_unit

    @property
    def net_total_price(self):
        return self.total_price - self.return_total_price

    @property
    def net_quantity(self):
        return self.quantity - self.return_quantity
    
