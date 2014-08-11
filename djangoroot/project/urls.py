
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.base import TemplateView

from shop import urls as shop_urls
from shop.models.productmodel import Product
from shop.views.order import ShopListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    (r'^shop/', include(shop_urls)),

    (r'^$', TemplateView.as_view(template_name='index.html')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    url(r'^hook/', include('github_hook.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

