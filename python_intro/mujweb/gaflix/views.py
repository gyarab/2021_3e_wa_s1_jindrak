from django.shortcuts import render
from django.template import context
from .models import Movie
from .models import Category

def movielist(request):
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'homepage.html', context)

def category_detail(request, category_id):
    context = {
        'movies': Movie.objects.filter(categories__id=category_id),
        'categories': Category.objects.all()
    }
    return render(request, 'homepage.html', context)
# Create your views here.
