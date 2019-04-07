from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='index'),
     path('account', views.account, name="account"),
    path('index', views.post_list, name="index"),

    path('wrapper', views.wrapper, name="wrapper"),
    path('wishlist', views.wishlist, name="wishlist"),
    path('checkout', views.checkout, name="checkout"),
    path('cart', views.cart, name="cart"),


]