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

# def ProduitCreate(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST)
#         if form.is_valid():
#             prdt = form.save()
#             return redirect('dtl_prdt', prdt.refProd)
#     else:
#         form = ProduitForm()
#     return render(request, "monApp/create_produit.html", {'form': form})

class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"

    def form_valid(self, form) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Création d'un nouveau produit"
        return context

class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_produit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Création d'une nouvelle catégorie"
        return context

    def form_valid(self, form) -> HttpResponse:
        cat = form.save()
        return redirect('categorie', cat.idCat)
    
class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_produit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Création d'un nouveau rayon"
        return context

    def form_valid(self, form) -> HttpResponse:
        ray = form.save()
        return redirect('rayon', ray.idRayon)
    
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('categories')

class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('rayons')

# def produit_delete(request, pk):
#     prdt = Produit.objects.get(pk=pk) # nécessaire pour GET et pour POST
#     if request.method == 'POST':
#         # supprimer le produit de la base de données
#         prdt.delete()
#         # rediriger vers la liste des produit
#         return redirect('lst_prdts')
#     # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
#     return render(request, 'monApp/delete_produit.html', {'object': prdt})
    

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

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Modification d'un produit"
        return context

    def form_valid(self, form) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)
    
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_produit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Modification d'une catégorie"
        return context

    def form_valid(self, form) -> HttpResponse:
        cat = form.save()
        return redirect('categorie', cat.idCat)
    
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_produit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Modification d'un rayon"
        return context

    def form_valid(self, form) -> HttpResponse:
        ray = form.save()
        return redirect('rayon', ray.idRayon)

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['param'] = f"Hello {self.kwargs.get('param')}"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['param'] = "About us..."
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class EmailView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(EmailView, self).get_context_data(**kwargs)
        context['param'] = "Email reçu !!!"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)

# class ContactView(TemplateView):
#     template_name = "monApp/page_home.html"
#     def get_context_data(self, **kwargs):
#         context = super(ContactView, self).get_context_data(**kwargs)
#         context['titreh1'] = "Contact us..."
#         return context

#     def post(self, request, **kwargs):
#          return render(request, self.template_name)
    
def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via TutoDjango Contact form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monApp.com'],)
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'param':titreh1, 'form':form})

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    # queryset = Produit.objects.filter(refProd=2)

    def get_queryset(self ) :
        return Produit.objects.select_related('categorie').select_related('status')

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "stats"

    
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cats"

    def get_queryset(self ) :
        return Categorie.objects.annotate(nb_produits=Count('produits'))
    
class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rays"

    def get_queryset(self):
        return Rayon.objects.prefetch_related(
            Prefetch("contenirs", queryset=Contenir.objects.select_related("refProd")))


    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt = []
        for rayon in context['rays']:
            total = 0
            for contenir in rayon.contenirs.all():
                total += contenir.produit.prixUnitaireProd * contenir.Qte
            ryns_dt.append({'ray': rayon,'total_stock': total})
                
        context['ryns_dt'] = ryns_dt
        return context


class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
    
class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits.all()
        return context

    def get_queryset(self):
        return Categorie.objects.annotate(nb_produits=Count('produits'))
    
class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"
    
class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "ray"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0

        for contenir in self.object.contenirs.all():
            total_produit = contenir.produit.prixUnitaireProd * contenir.qte
            prdts_dt.append({ 'produit': contenir.produit,
                              'qte': contenir.qte,
                              'prix_unitaire': contenir.produit.prixUnitaireProd,
                              'total_produit': total_produit} )
            total_rayon += total_produit
            total_nb_produit += contenir.qte
        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit

        return context

class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
  
class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

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
