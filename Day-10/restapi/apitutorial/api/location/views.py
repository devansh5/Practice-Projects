from django.shortcuts import render
import requests
# Create your views here.

def home(request):
   response=requests.get('https://api.covidindiatracker.com/state_data.json')
   trans=response.json()
   return render(request,"location/home.html",{"trans":trans})