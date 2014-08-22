from django.views.generic import ListView
from project.models import Piece, PieceCategory

import logging
logger = logging.getLogger(__name__)


class PieceListView(ListView):
    context_object_name = "pieces"

    def get_queryset(self):
        category = PieceCategory.objects.filter(name=self.kwargs['category_name'])
        return Piece.objects.filter(category=category)