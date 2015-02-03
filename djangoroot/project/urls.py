
from django.conf.urls import *
from django.conf import settings
from django.views.generic.base import TemplateView
from project import views
from project.views import PieceListView, AboutView, AccountView, ChargeView

from shop import urls as shop_urls
from shop.views import ShopListView
from shop.views.order import OrderListView

import logging

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    (r'^shop/', include(shop_urls)),
    (r'^pieces/(?P<category_name>[\+\w\.@-_]+)/', PieceListView.as_view()),

    (r'^$', PieceListView.as_view()),
    (r'^about/', AboutView.as_view()),
    (r'^account/', AccountView.as_view()),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'project/login.html'}, name="login"),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^contact/', include('contact_form.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^coin/', include('coin.urls')),
    url(r'^hook/', include('github_hook.urls')),

    (r'^charge', ChargeView.as_view()),
)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#          {'document_root': settings.MEDIA_ROOT}),
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )

