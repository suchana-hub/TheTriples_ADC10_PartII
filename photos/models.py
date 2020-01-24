from django.db import models

# Create your models here.
class Photos(models.Model):
    photo=models.ImageField(upload_to='images/',null=True)
    label=models.TextField()
    like=models.IntegerField(default=0)
    caption=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def valid_caption(self):
        return self.caption!=""
        
    def valid_like(self):
        return self.like>0
    
    def valid_caption(self):
        return self.caption!=""

class Album(models.Model):
    photos=models.ManyToManyField(Photos)
    date=models.DateField(auto_now=True)
    like=models.IntegerField(default=0)



    def count_photos(self):
        return self.photos.all().count()


 


