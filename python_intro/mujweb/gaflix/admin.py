from atexit import register
from django.contrib import admin
from .models import Movie, Actor, Director, Category
# Register your models here.

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Category)