from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db import models

from django_extensions.db.fields import UUIDField


class Coin(models.Model):
    owner = models.ForeignKey(User, related_name="coins")
    uuid = UUIDField(auto_created=True)


class CoinSettings(models.Model):
    mood_weight = models.DecimalField(decimal_places=2, max_digits=100, default=0.02)
    productivity_weight = models.DecimalField(decimal_places=2, max_digits=100, default=0.02)
    sales_weight = models.DecimalField(decimal_places=2, max_digits=100, default=0.02)
    points_per_coin = models.IntegerField(default=100)

    class Meta:
        verbose_name = "Coin Settings"
        verbose_name_plural = "Coin Settings"


class CoinStat(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=1000, editable=False)
    mood = models.IntegerField()
    productivity = models.IntegerField()
    sales = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.mood < 0 or self.mood > 100:
            raise ValidationError('Mood must have a value between 0 and 100')
        if self.productivity < 0 or self.productivity > 100:
            raise ValidationError('Productivity must have a value between 0 and 100')
        if self.sales < 0 or self.sales > 100:
            raise ValidationError('Sales must have a value between 0 and 100')


class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name="transactions_sent")
    receiver = models.ForeignKey(User, related_name="transactions_received")
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            transfer_coins = self.sender.coins.all()[:self.amount]
            Coin.objects.filter(pk__in=transfer_coins).update(owner=self.receiver)

        super(Transaction, self).save(*args, **kwargs)

    def buy_coins(self, user, amount):
        self.sender = User.objects.get(username=settings.SHOP_OWNER_USERNAME)
        self.receiver = user
        self.amount = amount
        self.save()

    def clean(self):
        if self.amount < 1:
            raise ValidationError('Transfer amount must be greater than 0')
        if self.sender.coins.count() < self.amount:
            raise ValidationError('The sender is trying to send more coins than he has.')


class FractionalCoin(models.Model):
    user = models.ForeignKey(User, related_name="factional_coins")
    amount = models.IntegerField()
