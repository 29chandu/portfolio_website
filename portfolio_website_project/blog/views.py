from django.shortcuts import render

from . import models

# Create your views here.

def all_blogs_view(request):
    blogs = models.Blog.objects.all()

    context = {'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context=context)