from django.db import models

# Model to store details of a person
class Details(models.Model):
    # Field to store the first name, with a maximum length of 50 characters
    firstName = models.CharField(max_length=50)
    
    # Field to store the last name, with a maximum length of 50 characters
    lastName = models.CharField(max_length=50)

    # String representation of the model, which will display the full name
    def __str__(self):
        return self.firstName + " " + self.lastName
