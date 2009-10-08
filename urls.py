from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #
    # url(r'^mydjangoproject/', include('foo.urls')),
    #
    # url(r'^$', 'django.views.generic.simple.direct_to_template', 
    #    {'template': 'index.html'}, name="home"),

    url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
