from django.urls import path
from .views import RegisterAPI, UserListView, UserDetail, LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('signup/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]
