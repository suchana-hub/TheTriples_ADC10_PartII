from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Profile
 
# Create your views here.
 

def photo_data(request):
    if request.method == "GET":
        photo = Profile.objects.all()
        dict = {
            "photos":list(photo.values("id", "account_name", "following", "followers", "image_avaliable"))
        }
        return JsonResponse({
            "result":dict
            }
            )
 

def get_photo(request, pk):
    if request.method == "GET":
        try:
            photo = Profile.objects.get(pk = pk)
            response = json.dumps([{'ID':photo.id, 'Name':photo.account_name, 'Following': photo.following, 'Followers':photo.followers, 'Avaliable':photo.image_avaliable}])
            return HttpResponse(response, content_type='text/json')
        except:
            return JsonResponse({"Error":"No photo with the given id found."})
 

@csrf_exempt
def add_photo(request):
    if request.method == "POST":
 
        new = json.loads(request.body)
        account_name = new['account_name']
        following = new['following']
        followers = new['followers']
        photo = Profile.objects.create(account_name=account_name, following = following, followers = followers)
        try:
            photo.save()
            return JsonResponse({"Success":"photo has been added successfully!"})
        except:
            return JsonResponse({"Error":"photo could not be added!"})
 

@csrf_exempt
def update(request, pk):
    photo = Profile.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"ID":photo.id,"account_name":photo.account_name,"following":photo.following,"followers":photo.followers,"image_avaliable":photo.image_avaliable})
    elif request.method == "PUT":
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        photo.account_name = update_data['account_name']
        photo.following = update_data['following']
        photo.followers = update_data['followers']
        photo.image_avaliable = update_data['image_avaliable']
        photo.save()
        return JsonResponse({"Success":"photo Successfully Updated!!"})
    elif request.method == "DELETE":
        photo.delete()
        return JsonResponse({"Success":"photo Successfully Deleted!!"})
 
 
def pagination(request, page_num, num_data):
    skip = num_data * (page_num - 1)
    photo = Profile.objects.all() [skip:(page_num*num_data)]
    dict = {
        "photos":list(photo.values("id", "account_name", "following", "followers", "image_avaliable"))
    }
    return JsonResponse(dict)
 