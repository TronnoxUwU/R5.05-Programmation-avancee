from django.urls import path
from . import views

urlpatterns = [
    path("home/<param>", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("produits/", views.ListProduits, name="produits"),
    path('categories/',views.ListCategories ,name='categories'),
    path('statuts/',views.ListStatuts,name='statuts'),
    path('rayons/',views.ListRayons,name='rayons'),
]
