# Generated by Django 4.0.2 on 2022-02-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gaflix', '0005_movie_description_alter_person_birth_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
