from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Fund

@receiver(post_migrate)
def create_default_funds(sender, **kwargs):
    default_funds = [
        {"name": "Cash", "opening_balance": 0.00},
        {"name": "UPI", "opening_balance": 0.00},
        {"name": "Credit", "opening_balance": 0.00},
    ]

    for fund in default_funds:
        Fund.objects.get_or_create(
            name=fund["name"],
            defaults={"opening_balance": fund["opening_balance"]}
        )
