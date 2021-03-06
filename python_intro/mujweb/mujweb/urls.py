"""mujweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from gaflix.views import movielist, category_detail, actorlist, sex_detail, movie_detail
from django.conf.urls.static import static

def mojeview(request, course_id):
    return HttpResponse("Ahoj")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movielist, name='homepage'),
    path('herci', actorlist, name='actorlist'),
    path('kategorie/<int:category_id>', category_detail, name='category_detail'),
    path('film/<int:movie_id>', movie_detail, name='movie_detail'),
    path('pohlavi/<int:sex_id>', sex_detail, name='sex_detail'),
    path('one', TemplateView.as_view(template_name='one.html'), name='one'),
    path('two', TemplateView.as_view(template_name='two.html'), name='two'),
    path('course/<int:course_id>', mojeview, name='course-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
