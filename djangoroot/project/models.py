from shop.models import Product
from django.db import models


class Piece(Product):
    hero_image = models.ImageField("Image", upload_to='uploads')
    sold = models.BooleanField(default=False)

    class Meta: pass