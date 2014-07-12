from django.conf.urls import patterns, include, url

from django.contrib import admin
from django_youtube import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expresopy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^youtube/', include('django_youtube.urls')),
)
