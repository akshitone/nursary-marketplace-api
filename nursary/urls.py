from django.contrib import admin
from django.urls import path, include
from core.views import PlantListCreateView, PlantListView, PlantDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('', PlantListView.as_view()),
    path('plants/', PlantListView.as_view()),
    path('plants/<int:pk>/', PlantDetail.as_view()),
    path('plants/create/', PlantListCreateView.as_view()),
    path('users/', include('core.urls')),
    path('order/', include('orders.urls')),
]
