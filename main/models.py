from django.db import models

class UserSignup(models.Model):
    full_name = models.CharField(max_length=50)  # Field for Full Name
    date_of_birth = models.DateField()  # Field for Date of Birth
    nationality = models.CharField(max_length=50)  # Field for Nationality
    phone_number = models.CharField(max_length=15)  # Field for Phone Number
    address_line_1 = models.CharField(max_length=100)  # Field for Address Line 1
    address_line_2 = models.CharField(max_length=100, blank=True)  # Field for Address Line 2
    city = models.CharField(max_length=50)  # Field for City
    state = models.CharField(max_length=50)  # Field for State
    country = models.CharField(max_length=50)  # Field for Country
    pin_code = models.CharField(max_length=10)  # Field for Pin Code
    gender = models.CharField(max_length=20)  # Field for Gender

    def __str__(self):
        return self.full_name
