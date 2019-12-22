from django.urls import path
from .views import register_page, login_page

app_name = 'user'

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
]
