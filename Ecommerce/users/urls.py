
from django.urls import path
from . import views


urlpatterns = [
    # JWT
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('get_user/', views.get_user, name="get_user"),
]
