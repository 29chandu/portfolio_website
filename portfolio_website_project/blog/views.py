from django.shortcuts import render

# Create your views here.

def all_blogs_view(request):

    context = {}
    return render(request, 'blog/all_blogs.html', context=context)