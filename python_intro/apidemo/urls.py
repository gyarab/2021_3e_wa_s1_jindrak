"""apidemo URL Configuration

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
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from datetime import datetime

api = NinjaAPI()

@api.get("/add")
def add_resource(request, a: int, b: int):
    return {"result": a + b}

@api.get("/time")
def time_resource(request):
    d = datetime.now()
    return{
        "datetime": d.isoformat(),
        "date": d.date(),
        "time": d.time(),
    }

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
