from django.urls import path
from .views import *

urlpatterns=[
    path('login',get_login),
    path('sign_up',get_sign_up),
    path('save_user',save_user)
]