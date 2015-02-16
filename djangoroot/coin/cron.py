import datetime
from coin.models import CoinStat
from django_cron import CronJobBase, Schedule


class UpdateStats(CronJobBase):
    RUN_EVERY_MINS = 1439

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'coin.update_stats'

    def do(self):
        stat = CoinStat.objects.latest('created')
        now = datetime.datetime.now()

        if stat.created.day != now.day:
            new_stat = CoinStat()
            new_stat.mood = stat.mood
            new_stat.sales = stat.sales
            new_stat.productivity = stat.productivity
            new_stat.value = stat.value
            new_stat.save()