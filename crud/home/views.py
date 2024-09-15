from django.shortcuts import get_object_or_404, redirect, render
from home.models import Details

# Create your views here.

# Home view: Handles form submission and rendering of the homepage
def home(request):
    if request.method == "POST":
        # Retrieve first and last name from POST request
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        
        # Create a new Details object and save it to the database
        ins = Details(firstName=firstName, lastName=lastName)
        ins.save()
        
        # Prepare context with success flag and name to display in the template
        context = {'success': True, 'name' : firstName}
    else:
        # If not a POST request, simply return a context indicating no success
        context = {'success': False}
    
    # Render the 'index.html' template with the context
    return render(request, 'index.html', context)

# View all records: Retrieves all entries from the Details model and displays them
def view(request):
    # Retrieve all entries from the Details model
    allName = Details.objects.all()
    
    # Prepare context with all retrieved names
    context = {'view': allName}
    
    # Render the 'view.html' template with the context
    return render(request, 'view.html', context)

# Update view: Handles updating a specific record based on its ID
def update(request, id):
    allName = get_object_or_404(Details, id=id)

    # If the request method is POST, update the existing record
    if request.method == "POST":
        allName.firstName = request.POST.get('firstName')
        allName.lastName = request.POST.get('lastName') 
        
        # Save the updated record to the database
        allName.save()
        
        # Redirect to the view page to display all records
        return redirect('view')
    
    # Render the 'update.html' template with the current details of the record
    return render(request, 'update.html', {'allName': allName})

# Delete view: Handles deleting a specific record based on its ID
def delete(request, id):
    # Get the record to be deleted, or return a 404 if it doesn't exist
    allName = get_object_or_404(Details, id=id)

    # If the request method is POST, delete the record
    if request.method == "POST":
        # Delete the record from the database
        allName.delete()
        
        # Redirect to the view page after deletion
        return redirect('view')
    
    # Render the 'delete.html' template to confirm deletion
    return render(request, 'delete.html', {'allName': allName})
