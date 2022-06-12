
from django.urls import path
from . import views


urlpatterns = [
    # JWT
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('products/', views.products, name='products'),
    path('products/<str:pk>/', views.product_detail, name='single_product'),

]
