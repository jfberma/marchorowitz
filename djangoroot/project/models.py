from shop.models import Product
from django.db import models


class PieceCategory(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, verbose_name='Hex Color Value (eg. #ff0000)')
    background_gradient_top = models.CharField(max_length=7, default='#0097d0', verbose_name='Hex Color Value For Top of Background Gradient')
    background_gradient_bottom = models.CharField(max_length=7, default='#ffc300', verbose_name='Hex Color Value For Bottom of Background Gradient')

    def __unicode__(self):
        return u'%s' % (self.name)


class Piece(Product):
    hero_image = models.ImageField("Image", upload_to='uploads')
    sold = models.BooleanField(default=False)
    year = models.CharField(max_length=10, null=True)
    dimensions = models.CharField(max_length=255, null=True)
    medium = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(PieceCategory, related_name="pieces", null=True)

    class Meta: pass