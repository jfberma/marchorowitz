import json

from coin.models import CoinStat, Transaction
from decimal import Decimal
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, View
from payments.models import Customer
from project.models import Piece, PieceCategory
from shop.models import Order

import logging
logger = logging.getLogger(__name__)


class PieceListView(ListView):
    context_object_name = "pieces"

    def get_queryset(self):
        try:
            category = PieceCategory.objects.filter(name=self.kwargs['category_name'])
        except KeyError:
            category = PieceCategory.objects.filter(name='blue')
        return Piece.objects.filter(category=category)


class AboutView(TemplateView):
    template_name = "project/about.html"

    def get_context_data(self, **kwargs):
        coin_stats = CoinStat.objects.all().order_by('-id')[:10][::-1]
        context = super(AboutView, self).get_context_data(**kwargs)
        context['coin_stats'] = coin_stats
        return context


class AccountView(TemplateView):
    template_name = "project/account.html"

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            orders = Order.objects.filter(user=self.request.user)
            context['orders'] = orders
        return context


class ChargeView(View):

    def post(self, request, *args, **kwargs):
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            customer = Customer.create(user=request.user, card=request.POST.get('stripeToken'))

        if customer.can_charge():
            customer.charge(Decimal(request.POST.get('amount')))

        coin_stat = CoinStat.objects.all().order_by('-id')[0]
        coins = float(request.POST.get('amount')) / coin_stat.value
        transaction = Transaction()
        Transaction.buy_coins(transaction, request.user, coins)

        response = {
            'status': 'success',
            'coins': request.user.coins.count()
        }

        return HttpResponse(json.dumps(response), mimetype='application/json')