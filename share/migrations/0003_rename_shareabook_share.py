# Generated by Django 4.2.11 on 2024-05-07 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_rename_share_shareabook'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShareABook',
            new_name='Share',
        ),
    ]
