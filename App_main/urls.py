from django.urls import path
from . import views

app_name = 'App_main'

urlpatterns = [
    path('', views.home, name='home'),
    path('prepare/', views.prepare, name='prepare'),
    path('cart/', views.cart_view, name='cart'),
    path('delete/<int:pk>/', views.delete_sys, name='delete'),


]