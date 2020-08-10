from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

from . import models

# Create your views here.

def all_blogs_view(request):
    blogs = models.Blog.objects.all()

    context = {'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context=context)

def display_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, pk=blog_id)

    context = {"blog": blog}
    return render(request, 'blog/display_blog.html', context=context)
