from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def product_view(request):
    return HttpResponse("<h1>Hi You can view the products below</h1>")