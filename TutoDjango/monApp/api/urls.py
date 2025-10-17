from monApp.api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.CategorieViewSet, basename='categorie')
router.register(r'produits', views.ProduitViewSet, basename='produit')
router.register(r'statuts', views.StatutViewSet, basename='statut')
router.register(r'rayons', views.RayonViewSet, basename='rayon')
router.register(r'contenirs', views.ContenirViewSet, basename='contenir')

urlpatterns = [path('', include(router.urls)), 
            #    path('categories/',views.CategorieAPIView.as_view(),name="api-categories"),
            #    path('categorie/<pk>/',views.CategorieDetailAPIView.as_view(),name="api-categorie"),

            #    path('produits/',views.ProduitAPIView.as_view(),name="api-produits"),
            #    path('produit/<pk>/',views.ProduitDetailAPIView.as_view(),name="api-produit"),

            #    path('statuts/',views.StatutAPIView.as_view(),name="api-statuts"),
            #    path('statut/<pk>/',views.StatutDetailAPIView.as_view(),name="api-statut"),

            #    path('rayons/',views.RayonAPIView.as_view(),name="api-rayons"),
            #    path('rayon/<pk>/',views.RayonDetailAPIView.as_view(),name="api-rayon"),

            #   path('contenirs/',views.ContenirAPIView.as_view(),name="api-contenirs"),
               ]