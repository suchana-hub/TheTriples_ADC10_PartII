from django.db import models

# Create your models here.
class Photos(models.Model):
    photo=models.ImageField(upload_to='images/')
    label=models.TextField()
    like=models.IntegerField(default=0)
    caption=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)
