from django.urls import path
from.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   path('add_photos/',get_add_photos),
   path('post_add_photos',post_add_photos),
   path('photos_home/',get_photos_home,name="photos_home"),
   path('delete_photos/<int:ID>/',delete_photos),
   path('update_photos/<int:ID>',get_update_photos),
   path('post_update_photos',post_update_photos),
   path('post_update_photos/<int:ID>',post_update_photos)
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)