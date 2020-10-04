from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from filer.models import *
from sito.models import Post, Galleria, Gallery, Televisione, Video, Episodio, Curriculum, Galleriapagina, Galleriatelevisione
from django.contrib.syndication.views import Feed


# Create your views here.

class TimelineView(ListView):
    queryset = Curriculum.objects.all()
    context_object_name = 'time_list'
    template_name = 'timeline.html'

class HomeView(ListView):
    queryset = Post.objects.all().order_by('-pub_date')[:5]
    context_object_name = 'post_list'
    template_name = 'home.html'

class BlogView(ListView):
    queryset = Post.objects.all().order_by('-pub_date')
    context_object_name = 'post_list'
    template_name = 'blog.html'
    paginate_by = 12

class BlogPageView(DetailView):
    queryset = Post.objects.all()
    #context_object_name = 'post'
    template_name = 'blogpage.html'

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        context['galleria_list'] = Galleria.objects.filter(post = context['post'].id)
        return context

class TelevisioneView(ListView):
    queryset = Televisione.objects.all()
    context_object_name = 'tv_list'
    template_name = 'televisione.html'

class TelevisionePageView(DetailView):
    queryset = Televisione.objects.all()
    context_object_name = 'televisione'
    template_name = 'televisionepage.html'

    def get_context_data(self, **kwargs):
        context = super(TelevisionePageView, self).get_context_data(**kwargs)
        context['video_list'] = Video.objects.filter(programma = context['televisione'].id)[:1]
        context['episodio_list'] = Episodio.objects.filter(programma = context['televisione'].id)[:4]
        #context['filer_list'] = Image.objects.filter(folder_id = context['televisione'].galleria_folder)
        context['galleriatelevisione_list'] = Galleriatelevisione.objects.filter(programma = context['televisione'].id)
        return context

class BioView(ListView):
    queryset = Galleriapagina.objects.filter(pagina = 'Biografia')
    context_object_name = 'galleriapagina_list'
    template_name = 'biografia.html'

class NinaView(ListView):
    queryset = Galleriapagina.objects.filter(pagina = 'un po di me')
    context_object_name = 'galleriapagina_list'
    template_name = 'nina.html'

def LibroView(request):
   return render_to_response('libro.html')

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts":posts, "tag":tag})

'''
class BlogFeed(Feed):
    title = "Giovanna Nina Palmieri | Official Web Site"
    description = "Some ramblings of mine"
    link = "/blog/feed/"

    def items(self):
        return Post.objects.all().order_by("-created")[:5]
    def item_title(self, item):
        return item.titolo
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id

        '''