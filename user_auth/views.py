from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def get_login(request):
    return render(request,'login.html')

def get_sign_up(request):
    return render(request,'sign_up.html')

def  save_user(request):
    user_name=request.POST['user_name']
    user_email=request.POST['user_email']
    user_password=request.POST['user_password']
    
    user=User.objects.create_user(user_name,user_email,user_password)
    user.save()
    return HttpResponse("<h2>User Created</h2>")

