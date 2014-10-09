from coin.views import MiningView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^award-point/$', MiningView.as_view(), name='award-point'),
)
