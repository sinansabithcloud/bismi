from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Stock, StockSet

@receiver(post_save, sender=Stock)
def create_stockset_for_new_stock(sender, instance, created, **kwargs):
    if created:
        StockSet.objects.create(name=instance.name).stock.set([instance])
