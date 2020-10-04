from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def IndexView(request):
    post_list = Post.objects.filter(active=True).order_by('-pub_date')
    context = {'post_list':post_list}
    return render(request, 'index.html', context)
