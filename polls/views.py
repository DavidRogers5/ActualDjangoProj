from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from collections import defaultdict

import requests
import re
from bs4 import BeautifulSoup  # Use BeautifulSoup for parsing HTML
import logging


def extract_and_draw_unicode_grid(url):
    # Fetch document content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch document: {response.status_code}")
        return

    # Extract text from HTML
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    # Use regex to find (x, char, y) triplets
    matches = re.findall(r'(\d+)\s*([^\d\s])\s*(\d+)', text)

    if not matches:
        print("No valid coordinates found!")
        return

    # Convert extracted values into integer coordinates
    points = [(int(x), char, int(y)) for x, char, y in matches]

    # Determine the grid's dimensions
    max_x = max(x for x, _, _ in points) + 1
    max_y = max(y for _, _, y in points) + 1

    # Create an empty grid filled with spaces
    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    # Place Unicode characters in the grid
    for x, char, y in points:
        grid[y][x] = char  # Flip y-axis to match expected output format

    # Print the grid
    print("Extracted Grid (secret message):")
    for row in grid:
        print("".join(row))  # Print each row as a line of text


def index(request): 
        
    google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    extract_and_draw_unicode_grid(google_doc_url)


    response = requests.get("https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net//api/FakeListing")

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
        
        api_url = 'https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net///api/CreateListing'  # Replace with your API endpoint URL
        data = {
            'name': NewItemName,
            # Add other necessary data for the insert operation
        }       
        response = requests.post(api_url, data=data)               

        response = requests.get("https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net//api/FakeListing")
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
        response = requests.get("https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net//api/FakeListing")

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
        
        api_url = 'https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net///api/UpdateListing'  # Replace with your API endpoint URL
        data = {
            'id': NewItemIDName,
            'name': ListItemName,
            # Add other necessary data for the insert operation
        }       
        response = requests.post(api_url, data=data)               

        response = requests.get("https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net//api/FakeListing")
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
        response = requests.get("https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net//api/FakeListing")

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
        
        api_url = 'https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net///api/DeleteListing'  # Replace with your API endpoint URL
        data = {
            'id': NewItemIDName,
            # Add other necessary data for the insert operation
        }       
        response = requests.post(api_url, data=data)               

        response = requests.get("https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net//api/FakeListing")
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
        response = requests.get("https://bableapi-linux-awhybugma5ghasb2.centralus-01.azurewebsites.net//api/FakeListing")

        json_dataObj = json.loads(response.text) 
        json_string = json.dumps(json_dataObj['recordset'] )   
        context = json.loads(json_string);  

        context2 = {}   
        num_keys = len(context)

        for i in range(num_keys): 
            context2[i] = context[i]

        context3 = {'data': context2}        
        return render(request, 'Delete.html', context3)






