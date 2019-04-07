from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.PROTECT)
    image = models.ImageField(upload_to='image_perfil', null=True, blank=True)

    def __str__(self):
        return self.user.first_name;
