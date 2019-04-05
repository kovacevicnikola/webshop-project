from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    context={
    }
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    return HttpResponse('<h1>About Page</h1>')