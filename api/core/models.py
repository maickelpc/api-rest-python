from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName;
