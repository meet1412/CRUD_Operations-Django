from django.contrib import admin
from django.urls import path, include
from home import views

# URL patterns for the application
urlpatterns = [
    # Home page: Maps to the home view, which handles form submission and homepage rendering
    path('', views.home, name='home'),
    
    # View records: Maps to the view view, which retrieves and displays all records from the Details model
    path('view', views.view, name='view'),
    
    # Update record: Maps to the update view, which allows updating a specific record based on its ID
    path('update/<int:id>/', views.update, name='update_records'),
    
    # Delete record: Maps to the delete view, which handles deletion of a specific record based on its ID
    path('delete/<int:id>/', views.delete, name='delete_records'),
]
