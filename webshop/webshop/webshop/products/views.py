from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm

from django.contrib.auth.models import User

from .models import Product
# Create your views here.

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object':obj
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    if request.user.is_authenticated:
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductForm(request.POST or None)
        
        context = {
            'form':form
        }
        return render(request, "products/product_create.html", context)
    else:
        return render(request, "home.html")

def product_change_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'object':obj,
        'form':form
    }
    return render(request, "products/product_change.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        'object':obj,
        }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, "products/product_list.html", context)

def product_featured_view(request):
    queryset = Product.objects.filter(featured=True)
    context = {
        'featured':queryset
    }
    return render(request, "products/product_featured.html", context)
