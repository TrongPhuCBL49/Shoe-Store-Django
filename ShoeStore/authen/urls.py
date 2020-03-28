from django.urls import path
from .views import register_page, login_page, guest_login_view
from django.contrib.auth.views import LogoutView


app_name = 'authen'

urlpatterns = [
    path('register/', register_page, name='register'),
    path('register/guest', guest_login_view, name='guest_register'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
