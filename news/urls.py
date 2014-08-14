from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import NewsListView, NewDetailView

urlpatterns = patterns('',
    url(r'^news/$', NewsListView.as_view() ),
    url(r'^new/(?P<pk>[0-9]+)/$', NewDetailView.as_view() ),
    # url(r'^snippets/(?P<pk>[0-9]+)$', 'snippet_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)