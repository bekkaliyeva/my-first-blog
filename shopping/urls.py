from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    path('account.html', include('blog.urls')),
    path('index.html', include('blog.urls')),
     path('wishlist.html', include('blog.urls')),
      path('cart.html', include('blog.urls')),
       path('checkout.html', include('blog.urls')),

]