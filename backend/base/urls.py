from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.getRoutes, name='routes'),
    path('products', view=views.getProducts, name='products'),
    path('products-db', view=views.getProductsListFromDB, name='products-db'),
    path('products/<str:pk>', view=views.getParticularProduct, name='particular-product'),
    path('products-db/<str:pk>', view=views.getProductsByIDFromDB, name='particular-product-db'),
]




