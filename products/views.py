from django.http import HttpResponse
from django.shortcuts import render

# /products ->

def index(request):
    return HttpResponse('Hello World')
