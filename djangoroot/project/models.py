from shop.models import Product
from django.db import models


class PieceCategory(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, verbose_name='Hex Color Value (eg. #ff0000)')

    def __unicode__(self):
        return u'%s' % (self.name)


class Piece(Product):
    hero_image = models.ImageField("Image", upload_to='uploads')
    sold = models.BooleanField(default=False)
    category = models.ForeignKey(PieceCategory, related_name="pieces", null=True)

    class Meta: pass