from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.

class Fund(models.Model):
    name = models.CharField(max_length=100)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name
    
    @property
    def income_from_sales(self):
        return sum(salesbill.total_amount_after_discount for salesbill in self.salesbills.all())
    
    
    @property
    def expense_from_purchases(self):
        return sum(purchase.net_total_price for purchase in self.purchases.all())
    
    @property
    def expenses_from_expenses(self):
        return sum(expense.amount for expense in self.expenses.all())
    
    @property
    def current_balance(self):
        return (self.opening_balance 
                + (self.income_from_sales)
                - (self.expense_from_purchases + self.expenses_from_expenses))

class ExpenseType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField()
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='expenses', default=1)
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, related_name='expenses', default=1)

    def __str__(self):
        return f"Expense of {self.amount} on {self.date}"