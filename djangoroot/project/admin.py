from django.contrib import admin

from models import PieceCategory
from models import Piece


class PieceCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'color')
    list_display = ('name',)
admin.site.register(PieceCategory, PieceCategoryAdmin)

class PieceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
admin.site.register(Piece, PieceAdmin)