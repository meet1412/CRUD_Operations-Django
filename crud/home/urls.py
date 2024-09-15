from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home , name='home'),
    path('view', views.view , name='view'),
    path('update/<int:id>/', views.update , name='update_records'),
    path('delete/<int:id>/', views.delete , name='delete_records'),
]
