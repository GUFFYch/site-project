# Generated by Django 4.0.4 on 2023-08-26 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_event_rate_sum_event_rating_event_vote_sum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='avalible',
            field=models.BooleanField(default=1, verbose_name='Есть в наличии \n (0 - нет | 1 - да)'),
        ),
        migrations.AddField(
            model_name='product',
            name='avalible',
            field=models.BooleanField(default=1, verbose_name='Есть в наличии (0 - нет | 1 - да)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rate_sum',
            field=models.IntegerField(default=0, verbose_name='Количество отзывов'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rating',
            field=models.FloatField(default=0.0, verbose_name='Рейтинг товара'),
        ),
        migrations.AlterField(
            model_name='event',
            name='vote_sum',
            field=models.IntegerField(default=0, verbose_name='Сумма отзывов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate_sum',
            field=models.IntegerField(default=0, verbose_name='Количество отзывов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0.0, verbose_name='Рейтинг товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vote_sum',
            field=models.IntegerField(default=0, verbose_name='Сумма отзывов'),
        ),
        migrations.CreateModel(
            name='CommentsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentator', models.TextField(blank=True, verbose_name='Имя покупателя')),
                ('review', models.CharField(default='', max_length=500)),
                ('rating', models.IntegerField(default='0')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='CommentsEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentator', models.TextField(blank=True, verbose_name='Имя покупателя')),
                ('review', models.CharField(default='', max_length=500)),
                ('rating', models.IntegerField(default='0')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.event')),
            ],
        ),
    ]