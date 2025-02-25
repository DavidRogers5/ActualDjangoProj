from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from collections import defaultdict


def index(request):
    
    response = requests.get("http://localhost:8080//api/FakeListing")

    json_dataObj = json.loads(response.text) 
    json_string = json.dumps(json_dataObj['recordset'] )   
    context = json.loads(json_string);  

    context2 = {}   
    num_keys = len(context)

    for i in range(num_keys): 
        context2[i] = context[i]

    context3 = {'data': context2}        
    return render(request, 'Home.html', context3) 

def create(request):

    if request.method == 'POST':
        NewItemName = request.POST.get('NewItemName')
        
        api_url = 'http://localhost:8080///api/CreateListing'  # Replace with your API endpoint URL
        data = {
            'name': NewItemName,
            # Add other necessary data for the insert operation
        }       
        response = requests.post(api_url, data=data)               

        response = requests.get("http://localhost:8080//api/FakeListing")
        json_dataObj = json.loads(response.text) 
        json_string = json.dumps(json_dataObj['recordset'] )   
        context = json.loads(json_string);  

        context2 = {}   
        num_keys = len(context)

        for i in range(num_keys): 
            context2[i] = context[i]

        context3 = {'data': context2}  
                   
        return render(request, 'Create.html', context3) 
  
    else:  
        response = requests.get("http://localhost:8080//api/FakeListing")

        json_dataObj = json.loads(response.text) 
        json_string = json.dumps(json_dataObj['recordset'] )   
        context = json.loads(json_string);  

        context2 = {}   
        num_keys = len(context)

        for i in range(num_keys): 
            context2[i] = context[i]

        context3 = {'data': context2}        
        return render(request, 'Create.html', context3) 

def update(request):

    if request.method == 'POST':
        NewItemIDName = request.POST.get('NewItemIDName')
        ListItemName = request.POST.get('ListItemName')
        
        api_url = 'http://localhost:8080///api/UpdateListing'  # Replace with your API endpoint URL
        data = {
            'id': NewItemIDName,
            'name': ListItemName,
            # Add other necessary data for the insert operation
        }       
        response = requests.post(api_url, data=data)               

        response = requests.get("http://localhost:8080//api/FakeListing")
        json_dataObj = json.loads(response.text) 
        json_string = json.dumps(json_dataObj['recordset'] )   
        context = json.loads(json_string);  

        context2 = {}   
        num_keys = len(context)

        for i in range(num_keys): 
            context2[i] = context[i]

        context3 = {'data': context2}  
                   
        return render(request, 'Update.html', context3) 
  
    else: 
        response = requests.get("http://localhost:8080//api/FakeListing")

        json_dataObj = json.loads(response.text) 
        json_string = json.dumps(json_dataObj['recordset'] )   
        context = json.loads(json_string);  

        context2 = {}   
        num_keys = len(context)

        for i in range(num_keys): 
            context2[i] = context[i]

        context3 = {'data': context2}        
        return render(request, 'Update.html', context3) 

def delete(request):
    
    if request.method == 'POST':
        NewItemIDName = request.POST.get('NewItemIDName')
        
        api_url = 'http://localhost:8080///api/DeleteListing'  # Replace with your API endpoint URL
        data = {
            'id': NewItemIDName,
            # Add other necessary data for the insert operation
        }       
        response = requests.post(api_url, data=data)               

        response = requests.get("http://localhost:8080//api/FakeListing")
        json_dataObj = json.loads(response.text) 
        json_string = json.dumps(json_dataObj['recordset'] )   
        context = json.loads(json_string);  

        context2 = {}   
        num_keys = len(context)

        for i in range(num_keys): 
            context2[i] = context[i]

        context3 = {'data': context2}  
                   
        return render(request, 'Delete.html', context3) 
  
    else:  
        response = requests.get("http://localhost:8080//api/FakeListing")

        json_dataObj = json.loads(response.text) 
        json_string = json.dumps(json_dataObj['recordset'] )   
        context = json.loads(json_string);  

        context2 = {}   
        num_keys = len(context)

        for i in range(num_keys): 
            context2[i] = context[i]

        context3 = {'data': context2}        
        return render(request, 'Delete.html', context3)






