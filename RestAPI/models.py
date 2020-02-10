from django.db import models
 
# Create your models here.
 
class Profile(models.Model):
    account_name= models.CharField(max_length=100)
    following=models.TextField()
    followers= models.TextField()
    image_avaliable=models.BooleanField(default=True)