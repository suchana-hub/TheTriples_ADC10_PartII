from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def get_login_page(req):
    return render(req,"login.html")

def get_sign_up_page(req):
    return render(req,"sign_up.html")


def post_sign_up(req):
    username=req.POST["username"]
    email=req.POST["email"]
    password=req.POST["password"]

    user=User.objects.create(username=username,email=email,password=password)

    user.save()

    return redirect("login")

def post_login(req):
    username=req.POST["username"]
    password=req.POST["password"]
    user=authenticate(username=username,password=password)
    print(user)
    if user is not None:
        return render(req,"profile.html")
    else:
        return redirect("login")




