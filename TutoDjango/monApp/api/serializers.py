from rest_framework import serializers
from monApp.models import *

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    produits = ProduitSerializer(many=True)
    class Meta:
        model = Categorie
        fields = ["idCat", "nomCat","produits"]

    def get_produits_categorie(self,instance):
        queryset = instance.produits.all()
        # Ne renvoyer les produits que si la catégorie en a au moins 2
        if queryset.count() < 2:
            return [] # moins de 2 produits on renvoie une liste vide→
        serializer = ProduitSerializer(queryset, many=True)
        return serializer.data

class StatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statut
        fields = '__all__'

class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = '__all__'

class ContenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenir
        fields = '__all__'