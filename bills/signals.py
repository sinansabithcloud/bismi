from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import SalesBillType

@receiver(post_migrate)
def create_default_sales_bill_types(sender, **kwargs):
    default_types = ['Wholesale', 'Retail']

    for bill_type in default_types:
        SalesBillType.objects.get_or_create(name=bill_type)
