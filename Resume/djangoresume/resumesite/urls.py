from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('cover-letter',views.cover_letter, name = 'cover_letter'),
    path('gallery',views.gallery, name = 'gallery')
    
]