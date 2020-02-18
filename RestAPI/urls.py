from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('photos/',views.get_add_photo),
    path('photos/<int:page_num>/<int:num_data>',views.pagination),
    path('photos/<int:pk>/',views.get_update_delete)
    ]