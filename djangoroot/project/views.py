from coin.models import CoinStat
from django.views.generic import ListView, TemplateView
from project.models import Piece, PieceCategory

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


class AccountView(TemplateView):
    template_name = "project/account.html"