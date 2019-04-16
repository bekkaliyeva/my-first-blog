from django.urls import path
from . import views

urlpatterns = [
    #index
    path('', views.index, name='index'),

    #for check
    path('wrapper', views.wrapper, name="wrapper"),

    path('products/<slug:type>/<slug:order>/', views.products, name="products"),
    path('quickview', views.quickview, name="quickview"),
    path('addCart/<int:prod_id>/', views.addTOcart, name="addCart"),
    path('Cart', views.cart, name="cart"),

    #register
    path('register', views.register, name='register'),


]