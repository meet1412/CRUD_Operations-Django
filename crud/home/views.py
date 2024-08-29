from django.shortcuts import render
from home import urls

# Create your views here.
def home(request):
    return render(request,'index.html')