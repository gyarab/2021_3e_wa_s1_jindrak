from django.contrib import admin

# from python_intro.mujweb.courses.models import Teacher
from .models import Teacher, Course

admin.site.register(Teacher)
admin.site.register(Course)