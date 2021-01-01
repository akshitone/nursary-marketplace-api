from django.contrib import admin
from django.urls import path, include
from core.views import PlantView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', PlantView.as_view(), name='test')
]