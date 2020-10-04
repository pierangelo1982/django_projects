from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from sito import views
from sito.models import Post
from sito.views import TimelineView, HomeView, BlogView, BlogPageView, TelevisioneView, TelevisionePageView, BioView, NinaView, LibroView
from django.views.generic import TemplateView
#from django.views.generic import ListView, DetailView

from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title = "Giovanna Nina Palmieri | Official Web Site"
    description = "Benvenuto nel sito di Nina Giovanna Palmieri, Giornalista, Autrice e conduttrice"
    link = "/blog/feed/"

    def items(self):
        return Post.objects.all().order_by("-pub_date")[:5]
    def item_title(self, item):
        return item.titolo
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id


urlpatterns = patterns('blog.views',
   url(r'^$', HomeView.as_view()),
   url(r'^blog/$', BlogView.as_view()), 
   url(r'^blog/(?P<pk>\d+)/$', BlogPageView.as_view()),
   url(r'^televisione/$', TelevisioneView.as_view()),
   url(r'^televisione/(?P<pk>\d+)/$', TelevisionePageView.as_view()),
   url(r'^timeline/$', TimelineView.as_view()),
   url(r'^biografia/$', BioView.as_view()),
   url(r'^nina/$', NinaView.as_view()),
   url(r'^book/$', TemplateView.as_view(template_name="libro.html")),
   #url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
   url(r'^feed/$', BlogFeed()),
   #url(r'^book/', LibroView),
   url(r'^contact/', include('contact_form.urls')),
   )

