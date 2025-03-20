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

    def __str__(self):
        return self.username
