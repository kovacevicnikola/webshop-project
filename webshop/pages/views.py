from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.contrib.auth.models import User

# Create your views here.

def home_view(request, *args, **kwargs):
    queryset = Product.objects.filter(featured=True)
    
    context = {
        'featured':queryset,
    }
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    return HttpResponse('<h1>About Page</h1>')