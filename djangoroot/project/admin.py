from django.contrib import admin

from models import PieceCategory
from models import Piece


class PieceCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'color', 'background_gradient_top', 'background_gradient_bottom')
    list_display = ('name',)
admin.site.register(PieceCategory, PieceCategoryAdmin)

class PieceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
admin.site.register(Piece, PieceAdmin)