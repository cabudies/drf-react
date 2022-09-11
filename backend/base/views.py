from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products as products_list
from .models import Product as ProductDBModel
from .serializers import ProductSerializer

# Create your views here.

@api_view(["GET"])
def getRoutes(request):
    return Response(
        'test'
    )


@api_view(["GET"])
def getProducts(request):
    return Response(products_list)


@api_view(["GET"])
def getProductsByIDFromDB(request, pk):
    products = ProductDBModel.objects.get(_id=pk)
    serialized_data = ProductSerializer(products, many=False)
    return Response(serialized_data.data)


@api_view(["GET"])
def getProductsListFromDB(request):
    products_list = ProductDBModel.objects.all()
    serialized_data = ProductSerializer(products_list, many=True)
    return Response(serialized_data.data)


@api_view(["GET"])
def getParticularProduct(request, pk):
    product = None
    for i in products_list:
        if i['_id'] == pk:
            product = i
            break

    return Response(product)
