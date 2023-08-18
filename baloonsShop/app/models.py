from django.db import models



class Event(models.Model):
    name = models.CharField(max_length=10000, name="Название праздника")
    explanation = models.TextField(name="Описание праздника")
    images = models.FileField(blank=True)
    price = models.IntegerField(name="Цена")
    
    def __str__(self):
        return f"Event object ({self.id})"

class EventImage(models.Model):
    image = models.ImageField(upload_to='static/images/EventImages/', name="Картинки")
    post = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=10000, name="Название товара")
    explanation = models.TextField(name="Описание товара")
    images = models.FileField(blank=True)
    price = models.IntegerField(name="Цена")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, name="Зависимость к празднику")

    def __str__(self):
        return f"Event object ({self.id})"

class ProductImage(models.Model):
    image = models.ImageField(upload_to='static/images/ProductEventImages/', name="Картинки")
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)