from django.urls import path
from . import views

name = 'account'

urlpatterns = [
    path('login/',views.user_login,name = 'login'),
]