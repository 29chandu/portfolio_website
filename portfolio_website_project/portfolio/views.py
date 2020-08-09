from django.shortcuts import render

from . import models

# Create your views here.
def home(request):

    projects = models.Project.objects.all()

    print(projects)

    context = {'projects': projects}

    return render(request, 'portfolio/index.html', context=context)