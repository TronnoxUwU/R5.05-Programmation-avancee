from django.urls import path
from django.views.generic import *
from . import views

urlpatterns = [
    # path('home/<param>', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('home', views.HomeView.as_view(), name='home'),
    path('home/<param>', views.HomeView.as_view(), name='home'),
    path('contact/',  views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('produits/', views.ListProduits, name='produits'),
    path('categories/',views.ListCategories ,name='categories'),
    path('statuts/',views.ListStatuts,name='statuts'),
    path('rayons/',views.ListRayons,name='rayons'),
]
