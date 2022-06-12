
from django.urls import path
from . import views


urlpatterns = [

    path('products/', views.products, name='products'),
    path('products/<str:pk>/', views.product_detail, name='single_product'),

]
