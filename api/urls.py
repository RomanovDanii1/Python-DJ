from django.urls import path
from .views import *

urlpatterns = [
    path('pet/', PetList.as_view()),
    path('pet/<int:pk>/', PetDetails.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetails.as_view()),
    path('payment/', PaymentList.as_view()),
    path('order/', OrderList.as_view()),
    path('users/', UserList.as_view()),
    path('orderitem/', OrderItemList.as_view()),
]