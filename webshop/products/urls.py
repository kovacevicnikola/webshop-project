from django.urls import path
from .views import (product_detail_view, 
                    product_featured_view, 
                    product_create_view, 
                    product_change_view, 
                    product_delete_view, 
                    product_list_view
)


app_name = 'products'
urlpatterns= [
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
    path('change/<int:id>/', product_change_view, name='product-change'),
    path('delete/<int:id>/', product_delete_view, name='product-delete'),
    path('list/', product_list_view, name='product-list'),
    path('featured/', product_featured_view, name='product-featured'),
    
]