from django.contrib import admin

from models import Coin
from models import CoinStat


class CoinAdmin(admin.ModelAdmin):
    fields = ('owner',)
    list_display = ('uuid', 'owner',)
admin.site.register(Coin, CoinAdmin)

admin.site.register(CoinStat)