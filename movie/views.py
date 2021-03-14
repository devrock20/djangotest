from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def function(request):
	hack=request.POST.get("movie","")
	url = "http://www.omdbapi.com/?apikey=218d69c2&t={0}".format(hack)
	r = requests.get(url)
	json_data = r.json()
	result = r.text
   
	return render(request,'movie/index.html',{'json_data':json_data}) 


def index(request):
	return render(request,'movie/index.html')