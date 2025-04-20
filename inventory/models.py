from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class StockType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    @property
    def no_of_stocks(self):
        return self.stocks.all().count()

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(unique=True, max_length=100)
    initial_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    supplier = models.CharField(max_length=100, blank=True, null=True)  # optional
    stock_type = models.ForeignKey(StockType, on_delete=models.CASCADE, related_name='stocks', null=True, blank=True)  # optional

    def __str__(self):
        return self.name
    
    @property
    def sold_quantity(self):
        return sum(stockset.sold_quantity for stockset in self.stocksets.all())

    @property
    def purchased_quantity(self):
        return sum(stockset.purchased_quantity for stockset in self.stocksets.all())
    
    @property
    def sales_return_quantity(self):
        return sum(stockset.sales_return_quantity for stockset in self.stocksets.all())

    @property
    def purchases_return_quantity(self):
        return sum(stockset.purchases_return_quantity for stockset in self.stocksets.all())
    
    @property
    def remaining_quantity(self):
        return (self.initial_quantity 
                + (self.purchased_quantity - self.purchases_return_quantity) 
                - (self.sold_quantity - self.sales_return_quantity))

class StockSet(models.Model):
    name = models.CharField(unique=True, max_length=100)
    stock = models.ManyToManyField(Stock, related_name='stocksets')

    def __str__(self):
        return self.name
    
    @property
    def stock_type(self):
        if self.stock.all().count() > 1:
            return "Set"
        else:
            return self.stock.first().stock_type.name if self.stock.first().stock_type else "unknown"
    
    @property
    def stock_pk(self):
        if self.stock_type == 'Set':
            return self.pk
        else:
            return self.stock.first().pk
    
    @property
    def cost_price(self):
        stocks = self.stock.all()
        if not stocks:
            return 0
        return sum(stock.cost_price for stock in stocks)
    
    @property
    def selling_price(self):
        stocks = self.stock.all()
        if not stocks:
            return 0
        return sum(stock.selling_price for stock in stocks)
    
    @property
    def initial_quantity(self):
        stocks = self.stock.all()
        if not stocks:
            return 0
        return min(stock.initial_quantity for stock in stocks)
    
    @property
    def sold_quantity(self):
        return sum(sale.quantity for sale in self.sales.all())
    
    @property
    def purchased_quantity(self):
        return sum(purchase.quantity for purchase in self.purchases.all())
    
    @property
    def sales_return_quantity(self):
        return sum(sale.return_quantity for sale in self.sales.all())
    
    @property
    def purchases_return_quantity(self):
        return sum(purchase.return_quantity for purchase in self.purchases.all())
    
    @property
    def remaining_quantity(self):
        stocks = self.stock.all()
        if not stocks:
            return 0
        return min(stock.remaining_quantity for stock in stocks)
    

