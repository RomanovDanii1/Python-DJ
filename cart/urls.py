from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add-item-to-cart/<slug:slug>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', views.make_order, name='make_order'),
]