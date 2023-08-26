from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, timedelta
from django.utils import timezone 


class Event(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Название праздника", unique=True)
    explanation = models.TextField(verbose_name="Описание праздника", blank=True)
    mainImage = models.ImageField(upload_to='app/static/images/EventImages/', verbose_name="Главное изображение")
    price = models.IntegerField(verbose_name="Цена")
    rate_sum = models.IntegerField(default=0, verbose_name="Количество отзывов")
    vote_sum = models.IntegerField(default=0, verbose_name="Сумма отзывов")
    rating = models.FloatField(default=0.0, verbose_name="Рейтинг товара")
    avalible = models.BooleanField(default=1, verbose_name="Есть в наличии \n (0 - нет | 1 - да)")
    
    class Meta:
        verbose_name = "Мероприяте"
        verbose_name_plural = "Мероприятия"
    
    def __str__(self):
        return f"{self.name}"

class EventImage(models.Model):
    image = models.ImageField(blank=True, upload_to='app/static/images/EventImages/', verbose_name="Картинки")
    post = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Картинка мероприятя"
        verbose_name_plural = "Картинки мероприятий"
    
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"

class CommentsEvent(models.Model):
    comentator = models.TextField(max_length="50", verbose_name="Имя покупателя", blank=True, default = '')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='Мероприятие')
    review = models.CharField(max_length=1500, default='')
    rating = models.IntegerField(default='0')
    created_data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Комментарий мероприятя"
        verbose_name_plural = "Комментарии мероприятий"
    
    def __str__(self):
        return f'Комментарий к {self.event.name} | Оценка: {self.rating} | Коментарий: {self.review[:200]}'

    def getData(self):
        return countTime(self.created_data)
        

class Product(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Название товара", unique=True)
    explanation = models.TextField(verbose_name="Описание товара", blank=True)
    mainImage = models.ImageField(upload_to='app/static/images/ProductEventImages/', verbose_name="Главное изображение")
    price = models.IntegerField(verbose_name="Цена")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Связанный праздник")
    rate_sum = models.IntegerField(default=0, verbose_name="Количество отзывов")
    vote_sum = models.IntegerField(default=0, verbose_name="Сумма отзывов")
    rating = models.FloatField(default=0.0, verbose_name="Рейтинг товара")
    avalible = models.BooleanField(default=1, verbose_name="Есть в наличии (0 - нет | 1 - да)")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"    
    
    def __str__(self):
        return f"{self.name}"

class ProductImage(models.Model):
    image = models.ImageField(blank=True, upload_to='app/static/images/ProductEventImages/', verbose_name="Картинки")
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Картинка товара"
        verbose_name_plural = "Картинки товаров"
    
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"

class CommentsProduct(models.Model):
    comentator = models.TextField(max_length="50", verbose_name="Имя покупателя", blank=True, default = '')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Мероприятие')
    review = models.CharField(max_length=1500, default='')
    rating = models.IntegerField(default='0')
    created_data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Комментарий товара"
        verbose_name_plural = "Комментарии товаров"
        
    def __str__(self):
        return f'Комментарий к {self.product.name}'

    def getData(self):
        return countTime(self.created_data)
        


class Request(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Имя заказчика") 
    contact = models.CharField(max_length=10000, verbose_name="Номер телефона")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанный праздник")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанный товар")
    
    class Meta:
        verbose_name = "Запрос на связь"
        verbose_name_plural = "Запросы на связь"
        
    def __str__(self):
        return f"{self.name} | {self.contact} "
    
class SiteSettings(models.Model):
    name = models.CharField(max_length=10000, verbose_name="Название магазина")
    logoImage = models.ImageField(blank=True, upload_to='app/static/images/', verbose_name="Логотип")
    descriptionmImage = models.ImageField(blank=True, upload_to='app/static/images/', verbose_name="Изображение в поле (О нас)")
    descriptionText = models.TextField(max_length=10000, verbose_name="Текст в поле (О нас)")
    
    class Meta:
        verbose_name = "настройки сайта"
        verbose_name_plural = "настройки сайта"
    
class CoruselImage(models.Model):
    image = models.ImageField(blank=True, upload_to='app/static/images/CoruselImages/', verbose_name="Картинки в карусель")
    post = models.ForeignKey(SiteSettings, default=None, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Зависимость к празднику")
    
    class Meta:
        verbose_name = "Картинка карусели изображений"
        verbose_name_plural = "Картинка карусели изображений"
        
    def __str__(self):
        return f"Картнка от {self.post} | {self.id}"
    
def countTime(dateCreate):
    now = timezone.now()
    time_difference = now - dateCreate

    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_parts = []
    if days > 0:
        time_parts.append(f"{days} дней ")
        hours = minutes = seconds = 0
    if hours > 0:
        time_parts.append(f"{hours} ч ")
    if minutes > 0:
        time_parts.append(f"{minutes} мин ")
        seconds = 0
    if seconds > 0:
        time_parts.append(f"{seconds} с ")

    formatted_time = " ".join(time_parts)
    return formatted_time + "назад"