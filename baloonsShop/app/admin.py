from django.contrib import admin
from .models import Event, Product, EventImage, ProductImage


class EventImageAdmin(admin.StackedInline):
    model = EventImage

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageAdmin]

    class Meta:
       model = Event

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    pass



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
       model = Product

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass