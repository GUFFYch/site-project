from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


admin.site.register(Request)


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


class CoruselImageAdmin(admin.StackedInline):
    model = CoruselImage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    inlines = [CoruselImageAdmin]

    class Meta:
       model = SiteSettings

@admin.register(CoruselImage)
class coruselImageAdmin(admin.ModelAdmin):
    pass