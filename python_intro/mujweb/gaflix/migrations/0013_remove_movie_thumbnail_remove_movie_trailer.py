# Generated by Django 4.0.1 on 2022-04-07 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaflix', '0012_movie_trailer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='trailer',
        ),
    ]
