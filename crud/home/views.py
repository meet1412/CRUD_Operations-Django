from django.shortcuts import render, HttpResponse
from home import urls

# Create your views here.
def home(request):
    return HttpResponse("Works")