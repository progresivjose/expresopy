from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PoliticsListView

urlpatterns = patterns('',
    url(r'^politics/$', PoliticsListView.as_view() ),
    # url(r'^new/(?P<pk>[0-9]+)/$', NewDetailView.as_view() ),
    # url(r'^snippets/(?P<pk>[0-9]+)$', 'snippet_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)