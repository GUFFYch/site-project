from django.db import models



class Event(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Название праздника", unique=True)
    explanation = models.TextField(verbose_name="Описание праздника")
    mainImage = models.ImageField(upload_to='app/static/images/EventImages/', verbose_name="Главное изображение")
    images = models.FileField(blank=True)
    price = models.IntegerField(verbose_name="Цена")
    
    def __str__(self):
        return f"{self.name}"

class EventImage(models.Model):
    image = models.ImageField(upload_to='app/static/images/EventImages/', verbose_name="Картинки")
    post = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"



class Product(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Название товара", unique=True)
    explanation = models.TextField(verbose_name="Описание товара")
    mainImage = models.ImageField(upload_to='app/static/images/ProductEventImages/', verbose_name="Главное изображение")
    images = models.FileField(blank=True)
    price = models.IntegerField(verbose_name="Цена")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, verbose_name="Зависимость к празднику")

    def __str__(self):
        return f"{self.name}"

class ProductImage(models.Model):
    image = models.ImageField(upload_to='app/static/images/ProductEventImages/', verbose_name="Картинки")
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"
