# Generated by Django 4.2.11 on 2024-05-05 18:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_options_alter_recipe_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]