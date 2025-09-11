from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from monApp.models import *

def home(request, param=""):
    if request.GET and request.GET.get("test"):
        raise Http404
    return HttpResponse(f"<h1>Hello {param}</h1>")

def contact(request):
    return render(request, 'monApp/contact.html')

def about(request):
    return render(request, 'monApp/about.html')

# def produits(request):
#     prdts = Produit.objects.all()
#     txt = ""
#     for p in prdts:
#         txt += f"<li>{p.intituleProd}</li> "
#     return HttpResponse(f"<ul>{txt}</ul>")

def accueil(request,param):
    return HttpResponse(f"<h1>Hello {param}! You're connected</h1>")

def ma_vue(request):
    return JsonResponse({'foo': 'bar'})

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html', {'prdts': prdts})

def ListCategories(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html', {'cats': cats})

def ListStatuts(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html', {'stats': stats})

def ListRayons(request):
    rays = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html', {'rays': rays})