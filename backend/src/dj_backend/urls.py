from accounts import views
from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from django.urls import path, include


# router = routers.DefaultRouter()
# router.register(r'accounts', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
