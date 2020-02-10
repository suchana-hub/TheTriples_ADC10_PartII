from django.urls import path
from .views import *

urlpatterns=[
    path("",get_home),
    path("login/",get_login_page,name="login"),
    path("sign_up/",get_sign_up_page),
    path("post_login",post_login),
    path("post_sign_up",post_sign_up),
    path("logout/",get_logout)
]