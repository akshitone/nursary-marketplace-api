from django.urls import path
from .views import OrderCreateView, OrderDetail, OrderListView

urlpatterns = [
    path('', OrderListView.as_view()),
    path('<int:pk>/', OrderDetail.as_view()),
    path('create/', OrderCreateView.as_view()),
]
