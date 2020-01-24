from django.db import models

# Create your models here.
class Photos(models.Model):
    photo=models.ImageField(upload_to='images/',null=True)
    label=models.TextField()
    like=models.IntegerField(default=0)
    caption=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)

class Album:
    photos=models.ManyToManyField(Photos)
    date=models.DateField(auto_now=True)
    like=models.IntegerChoices(default=0)


 


