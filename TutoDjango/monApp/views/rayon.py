from django.shortcuts import redirect
from monApp.models import Rayon,Contenir
from monApp.forms import RayonForm
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('rayons')

@method_decorator(login_required, name='dispatch')
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
    
class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rays"

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Rayon.objects.filter(nomRayon__icontains=query).prefetch_related(
                Prefetch("contenirs", queryset=Contenir.objects.select_related("refProd")))
        return Rayon.objects.prefetch_related(
            Prefetch("contenirs", queryset=Contenir.objects.select_related("refProd")))


    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt = []
        for rayon in context['rays']:
            total = 0
            for contenir in rayon.contenirs.all():
                total += contenir.refProd.prixUnitaireProd * contenir.qte
            ryns_dt.append({'ray': rayon,'total_stock': total})
                
        context['ryns_dt'] = ryns_dt
        return context

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
            total_produit = contenir.refProd.prixUnitaireProd * contenir.qte
            prdts_dt.append({ 'produit': contenir.refProd,
                              'qte': contenir.qte,
                              'prix_unitaire': contenir.refProd.prixUnitaireProd,
                              'total_produit': total_produit} )
            total_rayon += total_produit
            total_nb_produit += contenir.qte
        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit

        return context