from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product
 
# Create your views here.
 
# This function retrieves all the data from the database
def product_data(request):
    if request.method == "GET":
        product = Product.objects.all()
        dict = {
            "products":list(product.values("id", "product_title", "product_description", "product_type", "product_status"))
        }
        return JsonResponse(dict)
 
# This function returns a specific data from the database
def get_product(request, pk):
    if request.method == "GET":
        try:
            product = Product.objects.get(pk = pk)
            response = json.dumps([{'ID':product.id, 'Title':product.product_title, 'Description': product.product_description, 'Type':product.product_type, 'Status':product.product_status}])
            return HttpResponse(response, content_type='text/json')
        except:
            return JsonResponse({"Error":"No product with the given id found."})
 
# This functions helps to add data in product database
@csrf_exempt
def add_product(request):
    if request.method == "POST":
 
        new = json.loads(request.body)
        product_title = new['product_title']
        product_description = new['product_description']
        product_type = new['product_type']
        product = Product.objects.create(product_title=product_title, product_description = product_description, product_type = product_type)
        try:
            product.save()
            return JsonResponse({"Success":"product has been added successfully!"})
        except:
            return JsonResponse({"Error":"product could not be added!"})
 
# This functions helps to modify or remove a data from product database
@csrf_exempt
def update_api_data(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"ID":product.id,"product_title":product.product_title,"product_description":product.product_description,"product_type":product.product_type,"product_status":product.product_status})
    elif request.method == "PUT":
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        product.product_title = update_data['product_title']
        product.product_description = update_data['product_description']
        product.product_type = update_data['product_type']
        product.product_status = update_data['product_status']
        product.save()
        return JsonResponse({"Success":"product Successfully Updated!!"})
    elif request.method == "DELETE":
        product.delete()
        return JsonResponse({"Success":"product Successfully Deleted!!"})
 
 
def product_objects_pagination(request, page_num, num_data):
    skip = num_data * (page_num - 1)
    product = Product.objects.all() [skip:(page_num*num_data)]
    dict = {
        "products":list(product.values("id", "product_title", "product_description", "product_type", "product_status"))
    }
    return JsonResponse(dict)
 