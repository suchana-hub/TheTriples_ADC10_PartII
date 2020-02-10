from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('photos/',views.photo_data),
    path('photos/<int:pk>/',views.get_photo),
    path('photos/upload/',views.add_photo),
    path('photos/paginated/<int:page_num>/<int:num_data>',views.pagination),
    path('photos/update/<int:pk>/',views.update),
    ]