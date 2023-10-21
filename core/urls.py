from django.urls import path
from .views import create_transaction, user_login, user_logout, register
urlpatterns = [
    path('create/', create_transaction, name='create-transact'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]