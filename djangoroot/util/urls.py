from django.conf.urls import patterns, url

from djangoroot.util.views import GitHubHookView

urlpatterns = patterns('',
    url(r'github-hook/$', GitHubHookView.as_view()),
)