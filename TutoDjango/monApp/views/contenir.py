from django.shortcuts import redirect
from monApp.models import Contenir
from monApp.forms import ContenirForm, ContenirModifForm
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse

class ContenirCreateView(CreateView):
    model = Contenir
    form_class=ContenirForm
    template_name = "monApp/create_produit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un produit au rayon"
        return context

    def form_valid(self, form) -> HttpResponse:
        form.instance.idRayon_id = self.kwargs['pk']
        ray = form.save()
        return redirect('rayon', self.kwargs['pk'])
    
class ContenirDeleteView(DeleteView):
    model = Contenir
    template_name = "monApp/delete_rayon.html"

    def get_object(self, queryset=None):
        id_rayon = self.kwargs.get('pk')
        ref_prod = self.kwargs.get('prod')
        return get_object_or_404(Contenir, idRayon=id_rayon, refProd=ref_prod)

    def get_success_url(self):
        return reverse('rayon', kwargs={'pk': self.object.idRayon.idRayon})
    
class ContenirUpdateView(UpdateView):
    model = Contenir
    form_class=ContenirModifForm
    template_name = "monApp/update_produit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Modification de la contenace d'un produit"
        return context
    
    def get_object(self, queryset=None):
        id_rayon = self.kwargs.get('pk')   # premier paramètre de ton URL
        ref_prod = self.kwargs.get('prod') # deuxième paramètre de ton URL
        return get_object_or_404(Contenir, idRayon=id_rayon, refProd=ref_prod)

    def form_valid(self, form):
        instance = form.save(commit=False)  # pas encore sauvegardé en base
        if instance.qte > 0:
            # Si la quantité est zéro, supprime l'objet s'il existe déjà
            if instance.pk:
                instance.delete()
            # Redirige vers la page rayon (par ex) car objet supprimé
            return redirect('rayon', self.kwargs.get('pk'))
        else:
            # Sinon sauvegarde normalement
            instance.save()
            return redirect('rayon', instance.idRayon.idRayon)