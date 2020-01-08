from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
# Create your views here.

def get_login(request):
    return render(request,'login.html')

def post_login(request):
    user_name=request.POST['user_name']
    user_pass=request.POST['user_password']

    user=authenticate(username=user_name,password=user_pass)

    if user is not None:
        return HttpResponse("<h2>User Logged In</h2>")
    else:
        return redirect('./login')


def get_sign_up(request):
    return render(request,'sign_up.html')

def  save_user(request):
    user_name=request.POST['user_name']
    user_email=request.POST['user_email']
    user_password=request.POST['user_password']
    
    user=User.objects.create_user(user_name,user_email,user_password)
    user.save()
    return HttpResponse("<h2>User Created</h2>")

