# Generated by Django 5.1.1 on 2024-10-11 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_remove_register_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='logout',
        ),
    ]
