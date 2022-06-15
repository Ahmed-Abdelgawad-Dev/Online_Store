
from django.urls import path
from . import views


urlpatterns = [
    # Users' Endpoints
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('get_user/', views.get_user, name="get_user"),
    path('update_user/', views.update_user, name='update_user'),
    path('get_users/', views.get_users, name="get_users"),
    path('register_user/', views.register_user, name="register_user"),
]
