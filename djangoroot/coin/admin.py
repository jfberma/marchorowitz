from django.contrib import admin

from models import Coin, CoinSettings
from models import CoinStat
from models import Transaction


class CoinAdmin(admin.ModelAdmin):
    fields = ('owner',)
    list_display = ('uuid', 'owner',)
    list_editable = ('owner',)
admin.site.register(Coin, CoinAdmin)


class CoinStatAdmin(admin.ModelAdmin):
    list_display = ('value',)
    fields = ()

    def save_model(self, request, obj, form, change):
        coin_settings = CoinSettings.objects.get(pk=1)
        coin_stat = CoinStat.objects.all().order_by('-id')[0]
        mood_effect = (obj.mood - coin_stat.mood) * float(coin_settings.mood_weight)
        productivity_effect = (obj.productivity - coin_stat.productivity) * float(coin_settings.productivity_weight)
        sales_effect = (obj.sales - coin_stat.sales) * float(coin_settings.sales_weight)
        last_record = CoinStat.objects.latest('created')
        obj.value = float(last_record.value) + mood_effect + productivity_effect + sales_effect
        obj.save()
admin.site.register(CoinStat, CoinStatAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('created', 'sender', 'receiver', 'amount',)
admin.site.register(Transaction, TransactionAdmin)


class CoinSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'points_per_coin', 'mood_weight', 'productivity_weight', 'sales_weight',)
    list_editable = ('points_per_coin', 'mood_weight', 'productivity_weight', 'sales_weight',)
admin.site.register(CoinSettings, CoinSettingsAdmin)