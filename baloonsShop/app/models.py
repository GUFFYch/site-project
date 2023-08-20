from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Название праздника", unique=True)
    explanation = models.TextField(verbose_name="Описание праздника")
    mainImage = models.ImageField(upload_to='app/static/images/EventImages/', verbose_name="Главное изображение")
    price = models.IntegerField(verbose_name="Цена")
    
    def __str__(self):
        return f"{self.name}"

class EventImage(models.Model):
    image = models.ImageField(blank=True, upload_to='app/static/images/EventImages/', verbose_name="Картинки")
    post = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"



class Product(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Название товара", unique=True)
    explanation = models.TextField(verbose_name="Описание товара")
    mainImage = models.ImageField(upload_to='app/static/images/ProductEventImages/', verbose_name="Главное изображение")
    price = models.IntegerField(verbose_name="Цена")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, verbose_name="Связанный праздник")

    def __str__(self):
        return f"{self.name}"

class ProductImage(models.Model):
    image = models.ImageField(blank=True, upload_to='app/static/images/ProductEventImages/', verbose_name="Картинки")
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"


class Request(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Имя заказчика") 
    contact = models.CharField(max_length=10000, verbose_name="Номер телефона")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанный праздник")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанный товар")
    
    def __str__(self):
        return f"{self.name} | {self.contact} "
    
class SiteSettings(models.Model):
    
    name = models.CharField(max_length=10000, verbose_name="Название магазина")
    logoImage = models.ImageField(blank=True, upload_to='app/static/images/', verbose_name="Логотип")
    descriptionmImage = models.ImageField(blank=True, upload_to='app/static/images/', verbose_name="Изображение в поле (О нас)")
    descriptionText = models.TextField(max_length=10000, verbose_name="Текст в поле (О нас)")
    
class CoruselImage(models.Model):
    image = models.ImageField(blank=True, upload_to='app/static/images/CoruselImages/', verbose_name="Картинки в карусель")
    post = models.ForeignKey(SiteSettings, default=None, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, verbose_name="Зависимость к празднику")
    
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"