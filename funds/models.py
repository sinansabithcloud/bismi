from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db.models import Sum

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
        income = self.income_from_sales
        purchases = self.expense_from_purchases
        expenses = self.expenses_from_expenses
        transfers_out = self.transfers_out.aggregate(total=Sum('amount'))['total'] or 0
        transfers_in = self.transfers_in.aggregate(total=Sum('amount'))['total'] or 0

        return (self.opening_balance + income + transfers_in
                - (purchases + expenses + transfers_out))

    
    @property
    def current_balance_without_transfers(self):
        return (self.opening_balance 
                + (self.income_from_sales)
                - (self.expense_from_purchases + self.expenses_from_expenses))

class FundTransfer(models.Model):
    from_fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='transfers_out')
    to_fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='transfers_in')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.from_fund == self.to_fund:
            raise ValueError("Cannot transfer to the same fund.")

        if self.amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        if self.amount > self.from_fund.current_balance:
            raise ValueError("Insufficient balance in source fund.")

        super().save(*args, **kwargs)


class ExpenseType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Function to return the current date in local timezone (IST)
def get_current_date():
    return timezone.localtime(timezone.now()).date()

# Function to return the current time in local timezone (IST)
def get_current_time():
    return timezone.localtime(timezone.now()).time()

class Expense(models.Model):
    date = models.DateField(default=get_current_date)
    time = models.TimeField(default=get_current_time)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField()
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='expenses', default=1)
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, related_name='expenses', default=1)

    def __str__(self):
        return f"Expense of {self.amount} on {self.date}"