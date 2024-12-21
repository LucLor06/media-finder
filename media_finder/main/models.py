from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...

class Genre(models.Model):
    name = models.CharField(max_length=32)

class AbstractMedia(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        abstract = True
        
class Book(AbstractMedia):
    genres = models.ManyToManyField('Genre', related_name='books')
    
class Movie(AbstractMedia):
    genres = models.ManyToManyField('Genre', related_name='movies')
    
class Show(AbstractMedia):
    genres = models.ManyToManyField('Genre', related_name='shows')
    