# Generated by Django 5.1.1 on 2024-10-05 13:07

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name=models.AutoField(primary_key=True, verbose_name='Color')),
        ),
    ]
