from django.db import models


# Create your models here.
class Profile(models.Model):
    external_id = models.PositiveIntegerField(verbose_name='user id in social')
    name = models.TextField(verbose_name='user name')

    class Meta:
        verbose_name = 'Profile'
