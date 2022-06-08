from django.contrib import admin
from django.urls import path, include


# def index_view(request):
#     return render(request, 'build/index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # path('', index_view, name='index'),
]
