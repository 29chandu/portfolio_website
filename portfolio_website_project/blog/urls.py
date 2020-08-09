from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_blogs_view, name='all_blogs'),
]