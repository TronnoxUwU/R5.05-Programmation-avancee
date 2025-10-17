from monApp.models import Categorie
from rest_framework import viewsets
from .serializers import *
import datetime

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        datefilter = self.request.GET.get('datefilter')
        if datefilter is not None:
            datefilter=datetime.strptime(datefilter, "%d/%m/%Y")
            queryset = queryset.filter(dateFabProd__gt=datefilter)
        return queryset

class StatutViewSet(viewsets.ModelViewSet):
    queryset = Statut.objects.all()
    serializer_class = StatutSerializer

class RayonViewSet(viewsets.ModelViewSet):
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer

# class CategorieAPIView(generics.ListCreateAPIView):
#     queryset = Categorie.objects.all()
#     serializer_class = CategorieSerializer

# class CategorieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Categorie.objects.all()
#     serializer_class = CategorieSerializer

# class ProduitAPIView(generics.ListCreateAPIView):
#     queryset = Produit.objects.all()
#     serializer_class = ProduitSerializer

# class StatutAPIView(generics.ListCreateAPIView):
#     queryset = Statut.objects.all()
#     serializer_class = StatutSerializer

# class RayonAPIView(generics.ListCreateAPIView):
#     queryset = Rayon.objects.all()
#     serializer_class = RayonSerializer

# class ContenirAPIView(generics.ListCreateAPIView):
#     queryset = Contenir.objects.all()
#     serializer_class = ContenirSerializer

class ContenirViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer

# class ProduitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Produit.objects.all()
#     serializer_class = ProduitSerializer

# class StatutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Statut.objects.all()
#     serializer_class = StatutSerializer

# class RayonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rayon.objects.all()
#     serializer_class = RayonSerializer