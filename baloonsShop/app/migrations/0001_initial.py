# Generated by Django 3.2.19 on 2023-08-18 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Название праздника', models.CharField(max_length=255)),
                ('Описание праздника', models.TextField()),
                ('images', models.FileField(blank=True, upload_to='')),
                ('Цена', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Название товара', models.CharField(max_length=255)),
                ('Описание товара', models.TextField()),
                ('images', models.FileField(blank=True, upload_to='')),
                ('Цена', models.IntegerField()),
                ('Зависимость к празднику', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Картинки', models.ImageField(upload_to='static/images/ProductEventImages/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Картинки', models.ImageField(upload_to='static/images/EventImages/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
    ]
