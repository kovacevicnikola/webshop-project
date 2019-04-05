"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.conf import settings

from django.views.static import serve

from pages.views import home_view, about_view
from products.views import product_detail_view, product_featured_view, product_create_view, product_change_view, product_delete_view, product_list_view



urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('featured/', product_featured_view, name='Home'),
    path('about/', about_view, name='About'),
    path('product/<int:id>/', product_detail_view, name='product detail'),
    path('create/', product_create_view, name='product create'),
    path('change/<int:id>/', product_change_view, name='product change'),
    path('delete/<int:id>/', product_delete_view, name='product delete'),
    path('product_list/', product_list_view, name='product list'),
    
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT,}),


    ]
