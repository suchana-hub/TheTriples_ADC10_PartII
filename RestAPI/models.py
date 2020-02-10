from django.db import models
 
# Create your models here.
 
class Prod(models.Model):
    product_title= models.CharField(max_length=120)
    product_description=models.TextField()
    product_type= models.CharField(max_length=30)
    product_status=models.BooleanField(default=True)