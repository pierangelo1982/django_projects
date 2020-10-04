from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def IndexView(request):
    post_list = Post.objects.filter(active=True).order_by('-pub_date')
    html = []
    for p in post_list:
        html.append("<h1>" + p.titolo + "</h1>  <p>" + p.descrizione + "</p> <p><hr></p>")
    return HttpResponse(html)
