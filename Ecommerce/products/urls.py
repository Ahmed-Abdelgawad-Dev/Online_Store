
from django.urls import path
from . import views


urlpatterns = [
    # Products' endpoints
    path('', views.products, name='products'),
    path('<str:pk>/', views.product_detail, name='single_product'),

]
