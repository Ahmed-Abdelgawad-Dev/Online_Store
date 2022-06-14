
from django.urls import path
from . import views


urlpatterns = [
    # Products endpoints
    path('products/', views.products, name='products'),
    path('products/<str:pk>/', views.product_detail, name='single_product'),

]
