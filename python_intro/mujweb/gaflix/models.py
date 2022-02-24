from cProfile import label
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    movies = models.ManyToManyField('Movie', blank=True)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    csfd_rating = models.PositiveSmallIntegerField
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField('Actor')
    categories = models.ManyToManyField('Category')
    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name

class Actor(Person):
    class Meta:
        ordering = ['birth_date']
    #pass
class Director(Person):
    pass