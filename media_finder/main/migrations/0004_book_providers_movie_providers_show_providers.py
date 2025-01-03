# Generated by Django 5.1.4 on 2024-12-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_provider_book_country_of_origin_book_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='providers',
            field=models.ManyToManyField(blank=True, related_name='books', to='main.provider'),
        ),
        migrations.AddField(
            model_name='movie',
            name='providers',
            field=models.ManyToManyField(blank=True, related_name='movies', to='main.provider'),
        ),
        migrations.AddField(
            model_name='show',
            name='providers',
            field=models.ManyToManyField(blank=True, related_name='shows', to='main.provider'),
        ),
    ]
