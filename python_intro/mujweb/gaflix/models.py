from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    csfd_rating = models.PositiveSmallIntegerField
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField('Actor')
    categories = models.ManyToManyField('Category')

class Person(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Actor(Person):
    pass
class Director(Person):
    pass