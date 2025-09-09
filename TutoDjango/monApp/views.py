from django.shortcuts import render
from django.http import HttpResponse
from monApp.models import *

def home(request, param=""):
    return HttpResponse(f"<h1>Hello {param}</h1>")

def contact(request):
    return HttpResponse("<h1>Contact us</h1>")

def about(request):
    return HttpResponse("<h1>About us</h1>")

def produits(request):
    prdts = Produit.objects.all()
    txt = ""
    for p in prdts:
        txt += f"<li>{p.intituleProd}</li> "
    return HttpResponse(f"<ul>{txt}</ul>")