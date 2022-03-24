from django.shortcuts import render
from django.template import context
from .models import SEX_MALE, SEX_FEMALE, Movie
from .models import Category, Actor
from django.http import HttpResponseNotFound

def movielist(request):
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'homepage.html', context)

def actorlist(request):
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all(),
        'actors': Actor.objects.all(),
        'SEX_MALE': SEX_MALE,
        'SEX_FEMALE': SEX_FEMALE
    }
    return render(request, 'actors.html', context)

def category_detail(request, category_id):
    try:
        active_category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return HttpResponseNotFound("Category does not exist")
    context = {
        'movies': Movie.objects.filter(categories__id=category_id),
        'categories': Category.objects.all(),
        'active_category': active_category
    }
    return render(request, 'homepage.html', context)
# Create your views here.
