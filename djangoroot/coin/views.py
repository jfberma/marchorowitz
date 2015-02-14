import datetime
import json

from datetime import datetime as dt
from datetime import timedelta
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.base import View
from coin.models import Transaction, CoinSettings
from coin.models import Coin


class MiningView(View):

    def get(self, request):
        response_data = {}
        if request.user.pk is None:
            response_data['error'] = 'User must be logged in to mine'
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        response_data['points'] = request.session.get('points', 0)
        response_data['ppc'] = CoinSettings.objects.get(pk=1).points_per_coin
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    def post(self, request):
        response_data = {}
        if request.user.pk is None:
            response_data['error'] = 'User must be logged in to mine'
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        points = request.session.get('points', 0)

        #start fresh
        if points == 0:
            request.session['cheat_check'] = str(datetime.datetime.now())

        points += 1

        # check for cheating every x points
        if points % 50 == 0:
            last_check = dt.strptime(request.session.get('cheat_check'), '%Y-%m-%d %H:%M:%S.%f')
            # if you got x points in under 90 seconds, you're a fucking cheater
            if datetime.datetime.now() < (last_check + timedelta(seconds=90)):
                response_data['points'] = 0
                response_data['cheater'] = 'Stop cheating, you cheater!'
                request.session['points'] = 0
                request.session['cheat_check'] = str(datetime.datetime.now())
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            request.session['cheat_check'] = str(datetime.datetime.now())

        request.session['points'] = points
        response_data['points'] = points
        response_data['success'] = 'Good job!'

        if points % CoinSettings.objects.get(pk=1).points_per_coin == 0:
            transaction = Transaction()
            transaction.sender = User.objects.get(username=settings.SHOP_OWNER_USERNAME)
            transaction.receiver = request.user
            transaction.amount = 1
            response_data['award'] = 1
            transaction.save()
        return HttpResponse(json.dumps(response_data), content_type="application/json")