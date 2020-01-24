from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Permission
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login

from django.contrib.contenttypes.models import ContentType

from photos.models import Photos
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

    content_type=ContentType.objects.get_for_model(Photos)

    #add permission

    permission=Permission.objects.get(
        codename="add_student",
        content_type=content_type
    )

    user.user_permissions.add(permission)
    
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




