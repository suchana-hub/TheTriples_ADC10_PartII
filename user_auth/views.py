from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
# Create your views here.

def get_home(req):
    return render(req,"home.html")

def get_login_page(req):
    return render(req,"login.html")

def get_sign_up_page(req):
    return render(req,"sign_up.html")

def get_logout(req):
    logout(req)
    return redirect('login')

def post_sign_up(req):
    username=req.POST["username"]
    email=req.POST["email"]
    password=req.POST["password"]

    user=User.objects.create_user(username=username,email=email,password=password)

    user.save()

    return redirect("login")

def post_login(req):
    username=req.POST["username"]
    password=req.POST["password"]
    user=authenticate(username=username,password=password)
    if user is not None:
        login(req,user)
        return redirect("photos_home")
    else:
        return redirect("login")




