from coin.models import CoinStat
from django.views.generic import ListView, TemplateView
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
        coin_stats = CoinStat.objects.all()[:10]
        context = super(AboutView, self).get_context_data(**kwargs)
        context['coin_stats'] = coin_stats
        return context


class AccountView(TemplateView):
    template_name = "project/account.html"

    def get_context_data(self, **kwargs):
        orders = Order.objects.filter(user=self.request.user)
        context = super(AccountView, self).get_context_data(**kwargs)
        context['orders'] = orders
        return context