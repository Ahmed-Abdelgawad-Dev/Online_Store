
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.info),
    path('products/', views.products, name='products'),
    path('products/<str:pk>/', views.product_detail, name='single_product'),
    # JWT
    path('users/login/', views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    # path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
