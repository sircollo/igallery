# Generated by Django 4.0.4 on 2022-05-28 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_category_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gallery.category'),
        ),
    ]
