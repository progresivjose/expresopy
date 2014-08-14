from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expresopy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
