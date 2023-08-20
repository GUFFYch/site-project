# Generated by Django 4.2.4 on 2023-08-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_coruselimage_image_alter_eventimage_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='descriptionmImage',
            field=models.ImageField(blank=True, upload_to='app/static/images/', verbose_name='Изображение в поле (О нас)'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='logoImage',
            field=models.ImageField(blank=True, upload_to='app/static/images/', verbose_name='Логотип'),
        ),
    ]
