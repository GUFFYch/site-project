# Generated by Django 3.2.19 on 2023-08-18 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Название праздника',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='Зависимость к празднику',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.event'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Название товара',
            field=models.CharField(max_length=10000),
        ),
    ]