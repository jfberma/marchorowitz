import math
from coin.models import CoinStat


def dollars_to_coins(dollars):
    return math.ceil(dollars / CoinStat.objects.latest('created').value)