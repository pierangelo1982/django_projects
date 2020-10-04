from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sito.views.HomeView', name='home'),
    #url(r'^contact/$', 'sito.views.ContactView', name="contact"),
    url(r'^contact/$', 'sito.views.contacta', name="contact"),
    url(r'^contattaci/$', 'sito.views.contattaci', name="contattaci"),
    url(r'^iscriviti/$', 'sito.views.contactnews', name="newsletter"),
    url(r'^thanks/$', 'sito.views.Grazie', name="grazie"),



    #url(r'^', include(sito.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:  
        urlpatterns += patterns('',  
                                #REMOVE IT in production phase  
                                (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
                                {'document_root': settings.MEDIA_ROOT})
          )  
