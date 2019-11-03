from django.urls import path
from .views import home, logout, login, register

urlpatterns = [
    path('', home, name="home"),
    path('logout', logout, name='logout'),
    path('login', login, name='login'),
    path('register', register, name='user_register')
]