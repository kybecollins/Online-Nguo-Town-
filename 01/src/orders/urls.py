from django.contrib import admin
from django.urls import path,re_path

from django.conf import settings
from orders.views import checkout,order_view




app = "orders"

urlpatterns = [
   path('',order_view,name = 'orders'),
   path('checkout/',checkout,name = 'checkout')
    
]