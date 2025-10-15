from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from monApp.models import *
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from monApp.forms import *
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.urls import reverse

# def ProduitCreate(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST)
#         if form.is_valid():
#             prdt = form.save()
#             return redirect('dtl_prdt', prdt.refProd)
#     else:
#         form = ProduitForm()
#     return render(request, "monApp/create_produit.html", {'form': form})

# def produit_delete(request, pk):
#     prdt = Produit.objects.get(pk=pk) # nécessaire pour GET et pour POST
#     if request.method == 'POST':
#         # supprimer le produit de la base de données
#         prdt.delete()
#         # rediriger vers la liste des produit
#         return redirect('lst_prdts')
#     # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
#     return render(request, 'monApp/delete_produit.html', {'object': prdt})
    
# @login_required(login_url='/monApp/login/')
# def ProduitUpdate(request, pk):
#     prdt = Produit.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProduitForm(request.POST, instance=prdt)
#         if form.is_valid():
#             # mettre à jour le produit existant dans la base de données
#             form.save()
#             # rediriger vers la page détaillée du produit que nous venons de mettre à jour
#             return redirect('dtl_prdt', prdt.refProd)
#     else:
#         form = ProduitForm(instance=prdt)
#     return render(request,'monApp/update_produit.html', {'form': form})

# class ContactView(TemplateView):
#     template_name = "monApp/page_home.html"
#     def get_context_data(self, **kwargs):
#         context = super(ContactView, self).get_context_data(**kwargs)
#         context['titreh1'] = "Contact us..."
#         return context

#     def post(self, request, **kwargs):
#          return render(request, self.template_name)

# def home(request, param=""):
#     if request.GET and request.GET.get("test"):
#         raise Http404
#     return HttpResponse(f"<h1>Hello {param}</h1>")

# def contact(request):
#     return render(request, 'monAppstats/contact.html')

# def about(request):
#     return render(request, 'monApp/about.html')

# def produits(request):
#     prdts = Produit.objects.all()
#     txt = ""
#     for p in prdts:
#         txt += f"<li>{p.intituleProd}</li> "
#     return HttpResponse(f"<ul>{txt}</ul>")

# def accueil(request,param):
#     return HttpResponse(f"<h1>Hello {param}! You're connected</h1>")

# def ma_vue(request):
#     return JsonResponse({'fur': 'bar'})

# def ListProduits(request):
#     prdts = Produit.objects.all()
#     return render(request, 'monApp/list_produits.html', {'prdts': prdts})

# def ListCategories(request):
#     cats = Categorie.objects.all()
#     return render(request, 'monApp/list_categories.html', {'cats': cats})

# def ListStatuts(request):
#     stats = Statut.objects.all()
#     return render(request, 'monApp/list_statuts.html', {'stats': stats})

# def ListRayons(request):
#     rays = Rayon.objects.all()
#     return render(request, 'monApp/list_rayons.html', {'rays': rays})
