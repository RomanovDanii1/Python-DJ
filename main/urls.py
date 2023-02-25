from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', MainIndex.as_view(), name='home'),
    path('about/', MainAbout.as_view(), name='about'),
    path('contacts/', views.buy_information, name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('how_buy', views.buy_information, name='how_buy'),
    path('category/<slug:cat_slug>/', MainCategory.as_view(), name='category'),
    path('post/<slug:post_slug>', MainPost.as_view(), name='post')
]