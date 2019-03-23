from django.db import models
from django.auth import User


# class Permission(models.Model):
#     id = models.AutoField(primary_key=True)
#     permission = models.CharField(max_length=20)
#     description = models.CharField(max_length=100)
#     active = models.BooleanField(default=True)
#
#
# class Role(models.Model):
#     id = models.AutoField(primary_key=True)
#     role = models.CharField(max_length=20)
#     description = models.CharField(max_length=100)
#     active = models.BooleanField(default=True)
#     permissions = models.ManyToManyField(Permission, related_name='permissions')
#
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     email = models.CharField(max_length=150, unique=True, null=True)
#     password = models.CharField(max_length=255)
#     role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True, related_name='roles')
#     foto = models.ImageField(upload_to='image_perfil', null=True, blank=True)
#
#     def __str__(self):
#         return self.firstName;
