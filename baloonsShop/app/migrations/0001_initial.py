# Generated by Django 4.0.4 on 2023-08-23 18:31

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
                ('name', models.CharField(max_length=10000, unique=True, verbose_name='Название праздника')),
                ('explanation', models.TextField(blank=True, verbose_name='Описание праздника')),
                ('mainImage', models.ImageField(upload_to='app/static/images/EventImages/', verbose_name='Главное изображение')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000, unique=True, verbose_name='Название товара')),
                ('explanation', models.TextField(blank=True, verbose_name='Описание товара')),
                ('mainImage', models.ImageField(upload_to='app/static/images/ProductEventImages/', verbose_name='Главное изображение')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.event', verbose_name='Связанный праздник')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000, verbose_name='Название магазина')),
                ('logoImage', models.ImageField(blank=True, upload_to='app/static/images/', verbose_name='Логотип')),
                ('descriptionmImage', models.ImageField(blank=True, upload_to='app/static/images/', verbose_name='Изображение в поле (О нас)')),
                ('descriptionText', models.TextField(max_length=10000, verbose_name='Текст в поле (О нас)')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000, verbose_name='Имя заказчика')),
                ('contact', models.CharField(max_length=10000, verbose_name='Номер телефона')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.event', verbose_name='Связанный праздник')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product', verbose_name='Связанный товар')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='app/static/images/ProductEventImages/', verbose_name='Картинки')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='app/static/images/EventImages/', verbose_name='Картинки')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
        migrations.CreateModel(
            name='CoruselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='app/static/images/CoruselImages/', verbose_name='Картинки в карусель')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.event', verbose_name='Зависимость к празднику')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.sitesettings')),
            ],
        ),
    ]
