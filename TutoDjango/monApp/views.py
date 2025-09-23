from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from monApp.models import *
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from monApp.forms import ContactUsForm
from django.core.mail import send_mail

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
        return Produit.objects.order_by("prixUnitaireProd")

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "stats"

    
class CategorietListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cats"
    
class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rays"


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
    
class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"
    
class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "ray"

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
