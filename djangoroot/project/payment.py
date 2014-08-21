"""Payment backend that uses a users coins"""

from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from coin.models import Transaction

from shop.util.decorators import on_method, shop_login_required, order_required

import logging
logger = logging.getLogger(__name__)


class PayWithCoinsBackend(object):

    backend_name = "Pay With Coins"
    backend_verbose_name = _("Pay With Coins")
    url_namespace = "pay-with-coins"

    def __init__(self, shop):
        self.shop = shop
        # This is the shop reference, it allows this backend to interact with
        # it in a tidy way (look ma', no imports!)

    @on_method(shop_login_required)
    @on_method(order_required)
    def simple_view(self, request):
        """
        This simple view does nothing but record the "payment" as being
        complete since we trust the delivery guy to collect money, and redirect
        to the success page. This is the most simple case.
        """
        # Get the order object
        the_order = self.shop.get_order(request)
        user_balance = len(request.user.coins.all())

        if user_balance < the_order.order_total:
            return HttpResponseRedirect(reverse('cart') + '?err=insufficient_balance')

        # Create transaction
        transaction = Transaction()
        transaction.sender = request.user
        transaction.receiver = User.objects.get(username=settings.SHOP_OWNER_USERNAME)
        transaction.amount = the_order.order_total
        transaction.save()

        # Mark items as sold
        for item in the_order.items.all():
            product = item.product
            product.sold = True
            product.save()

        # Let's mark this as being complete for the full sum in our database
        # Set it as paid (it needs to be paid to the delivery guy, we assume
        # he does his job properly)
        self.shop.confirm_payment(
            the_order, self.shop.get_order_total(the_order), "None",
            self.backend_name)
        return HttpResponseRedirect(self.shop.get_finished_url())

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.simple_view, name='pay-with-coins'),
        )
        return urlpatterns
