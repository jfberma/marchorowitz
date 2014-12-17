from coin.models import Transaction
from coin.util import dollars_to_coins
from django.dispatch import receiver
from django.db.models.signals import post_save
from payments.models import Charge


@receiver(post_save, sender=Charge)
def card_charged_callback(sender, instance, created, **kwargs):
    if instance.receipt_sent:
        transaction = Transaction()
        transaction.buy_coins(instance.customer.user, dollars_to_coins(instance.amount))