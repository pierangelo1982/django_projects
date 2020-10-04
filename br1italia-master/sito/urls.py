'''
from django.conf.urls import patterns, include, url
from django.conf import settings
from sito import views
from sito.views import *
#from django.contrib import admin



urlpatterns = patterns('sito.views',
	url(r'^$', HomeView, name="home"),
	#url(r'^admin/', include(admin.site.urls)),

	
	url(r'^acqua/$', AcquaView, name="acqua"),
	url(r'^legno/$', LegnoView, name="legno"),
	url(r'^fuoco/$', FuocoView, name="fuoco"),
	url(r'^terra/$', TerraView, name="terra"),
	url(r'^metallo/$', MetalloView, name="metallo"),
	url(r'^(?P<post_id>\d+)/$', DettaglioView, name="dettaglio"),
	url(r'^contatti/$', ContattiView, name="contatti"),
	url(r'^consulenze/$', ConsulenzaView, name="consulenze"),
	url(r'^location/$', LocationView, name="location"),
	url(r'^blog/$', BlogView, name="blog"),
	url(r'^blog/(?P<post_id>\d+)/$', BlogDettaglioView, name="blogdettaglio"),
	url(r'^ckeditor/', include('ckeditor.urls')),
	
)

'''