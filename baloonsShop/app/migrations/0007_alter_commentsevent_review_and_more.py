# Generated by Django 4.0.4 on 2023-08-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_commentsevent_comentator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsevent',
            name='review',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='commentsproduct',
            name='review',
            field=models.CharField(default='', max_length=1500),
        ),
    ]
