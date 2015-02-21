from django.contrib import admin

from models import PieceCategory
from models import Piece
from suit.admin import SortableModelAdmin


class PieceCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'color', 'background_gradient_top', 'background_gradient_bottom')
    list_display = ('name',)
admin.site.register(PieceCategory, PieceCategoryAdmin)

class PieceAdmin(SortableModelAdmin):
    list_display = ('name', 'category')
    sortable = 'order'
admin.site.register(Piece, PieceAdmin)