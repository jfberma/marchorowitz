from django.contrib import admin

from models import Coin
from models import CoinStat
from models import Transaction


class CoinAdmin(admin.ModelAdmin):
    fields = ('owner',)
    list_display = ('uuid', 'owner',)
    list_editable = ('owner',)
admin.site.register(Coin, CoinAdmin)

admin.site.register(CoinStat)
admin.site.register(Transaction)