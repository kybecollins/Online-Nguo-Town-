from django.contrib import admin
from django.urls import path
from accounts.views import logout_default_view,login_default_view,registration_default_view


app = "accounts"
urlpatterns = [
   
    # path('login/' ),
    path('logout/',logout_default_view,name ='logout_view'),
    path('login/',login_default_view,name ='login_view'),
    path('register/',registration_default_view,name ='register_view'),
]
