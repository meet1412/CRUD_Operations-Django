from django.shortcuts import render
from home.models import Details

# Create your views here.
def home(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        ins = Details(firstName=firstName, lastName=lastName)
        ins.save()
        context = {'success': True}
    else:
        context = {'success': False}
    return render(request,'index.html', context)

def edit(request):
    return render(request, 'edit.html')