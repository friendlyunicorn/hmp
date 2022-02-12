from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Name')
    is_salesman = models.BooleanField(default=False, verbose_name='Is Salesman')
    verification = models.BooleanField(default=False, verbose_name='Verification')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'