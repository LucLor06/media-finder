from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import STATIC_URL
from config.settings import MEDIA_ROOT
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    ...

class AbstractModel(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Genre(AbstractModel):
    tmdb_id = models.PositiveBigIntegerField()
    
def provider_icon_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f'icons/providers/{slugify(instance.name)}.{ext}'
    
class Provider(AbstractModel):
    parent_provider = models.ForeignKey('Provider', blank=True, null=True, related_name='child_providers', on_delete=models.SET_NULL)
    icon = models.ImageField(upload_to=provider_icon_upload_to)
    tmdb_id = models.PositiveBigIntegerField()

class AbstractMedia(AbstractModel):
    year_released = models.PositiveIntegerField()
    synopsis = models.TextField()
    country_of_origin = models.CharField(max_length=64)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        abstract = True
        
    def __str__(self):
        return f'{self.name} ({self.year_released})'
    
    
def book_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f'books/{slugify(instance.name)}.{ext}'
        
class Book(AbstractMedia):
    genres = models.ManyToManyField('Genre', related_name='books')
    providers = models.ManyToManyField('Provider', blank=True, related_name='books')
    image = models.ImageField(upload_to=book_image_upload_to)


def movie_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f'movies/{slugify(instance.name)}.{ext}'
        
class Movie(AbstractMedia):
    genres = models.ManyToManyField('Genre', related_name='movies')
    providers = models.ManyToManyField('Provider', blank=True, related_name='movies')
    image = models.ImageField(upload_to=movie_image_upload_to)


def show_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f'shows/{slugify(instance.name)}.{ext}'

class Show(AbstractMedia):
    genres = models.ManyToManyField('Genre', related_name='shows')
    providers = models.ManyToManyField('Provider', blank=True, related_name='shows')
    image = models.ImageField(upload_to=show_image_upload_to)
    tmdb_id = models.PositiveBigIntegerField(default=0)
    seasons = models.PositiveIntegerField(default=1)
    was_canceled = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=True)
    
