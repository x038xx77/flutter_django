from django.db import models

# Create your models here.


class Profile(models.Model):
    """ User profile model """
    login = models.CharField(max_length=50, unique=True)
    channel_name = models.CharField(max_length=250, unique=True)
