from django.shortcuts import redirect, render
from home.models import Details

# Create your views here.
def home(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        ins = Details(firstName=firstName, lastName=lastName)
        ins.save()
        context = {'success': True, 'name' : firstName}
    
    else:
        context = {'success': False}
    return render(request,'index.html', context)

def view(request):
    allName = Details.objects.all()
    context = {'view': allName}
    return render(request, 'view.html', context)

def update(request, id):
    allName = Details.objects.get(id = id)

    if request.method == "POST":
        allName.firstName = request.POST.get['firstName']
        allName.lastName = request.POST.get['lastName'] 
        allName.save()
        return redirect('view')