from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /products ->

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def products_new(request):
    return HttpResponse('New Products')

