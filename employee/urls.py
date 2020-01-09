from django.urls import path
from .models import Employee
from .views import *
urlpatterns=[
    path('',employee_index),
    path('add/',emp_add_form),
    path('update/',emp_update_form)
]