from django.db import models

class UserSignup(models.Model):
    name: models.CharField(max_length=50)
    dateOfBirth: models.DateField()
    nationality: models.CharField(max_length=50)
    phone: models.CharField(max_length=15)
    line1: models.CharField(max_length=50)
    line2: models.CharField(max_length=50)
    city: models.CharField(max_length=50)
    state: models.CharField(max_length=50)
    country: models.CharField(max_length=50)
    pin: models.CharField(max_length=50)
    email: models.CharField(max_length=50)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=255)  # New field for Full Name
    dob = models.DateField()  # New field for Date of Birth
    nationality = models.CharField(max_length=100)  # New field for Nationality
    phone_number = models.CharField(max_length=15)  # New field for Phone Number
    address_line1 = models.CharField(max_length=255)  # New field for Address Line 1
    address_line2 = models.CharField(max_length=255, blank=True)  # New field for Address Line 2
    city = models.CharField(max_length=100)  # New field for City
    state = models.CharField(max_length=100)  # New field for State
    country = models.CharField(max_length=100)  # New field for Country
    pin_code = models.CharField(max_length=10)  # New field for Pin Code
    gender = models.CharField(max_length=10)  # New field for Gender

    def __str__(self):
        return self.username
