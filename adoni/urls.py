from django.conf.urls import patterns, include, url
from django.contrib import admin
from time_of_us.views import time_of_us
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adoni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'time-of-us', time_of_us)
)
