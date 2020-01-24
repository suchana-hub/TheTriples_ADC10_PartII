from django.db import models
from django.contrib.auth.models import User
from photos.models import Photos
# Create your models here.

class Profile:
    account=models.OneToOneField(User,on_delete=models.CASCADE)
    following=models.ForeignKey(User,on_delete=models.CASCADE)
    followers=models.ForeignKey(User,on_delete=models.CASCADE)
    photos=models.ForeignKey(Photos,on_delete=models.CASCADE)