from django.contrib.auth.models import User

from django.db import models

from django_extensions.db.fields import UUIDField


class Coin(models.Model):
    owner = models.ForeignKey(User, related_name="coins")
    uuid = UUIDField(auto_created=True)

class CoinStat(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=1000)