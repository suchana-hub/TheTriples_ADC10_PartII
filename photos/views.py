from django.shortcuts import render,redirect
from .models import Photos
from django.core.files.storage import FileSystemStorage

# Create your views here.
def get_add_photos(req):
    return render(req,'add_photos.html')

def get_update_photos(req,ID):
    photos=Photos.objects.get(id=ID)
    context={
        "photos":photos
    }
    return render(req,"update_photos.html",context=context)

def post_update_photos(req,ID):
    label=req.POST["label"]
    caption=req.POST["caption"]

    image=req.FILES['photo']
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    url=fs.url(filename)





    photos=Photos.objects.get(id=ID)

    photos.label=label
    photos.caption=caption
    photos.photo=url

    photos.save()

    return redirect("photos_home")  

def delete_photos(req,ID):
    photos=Photos.objects.get(id=ID)
    photos.delete()
    return redirect("photos_home")


def post_add_photos(req):
    label=req.POST["label"]
    caption=req.POST["caption"]

    image=req.FILES['photo']
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    url=fs.url(filename)


    new_photos=Photos(label=label,caption=caption,photo=url)
    new_photos.save()

    return redirect('photos_home')

def get_photos_home(req):
    all_photos=Photos.objects.all()
    if 'query_lable' in req.GET:
        all_photos=Photos.objects.filter(label=req.GET['query_lable'])

    context={
        "photos":all_photos
    }
    return render(req,'photos_home.html',context=context)
    