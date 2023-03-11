from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.profile_view, name='information'),
    path('orders/', views.orders_view, name='orders'),
    path('edit/', EditProfileView.as_view(), name='edit'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),
]