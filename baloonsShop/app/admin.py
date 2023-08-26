from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


admin.site.register(Request)
admin.site.register(CommentsEvent)
admin.site.register(CommentsProduct)

# start of event sector
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

class CommentsInline(admin.TabularInline):
    model = CommentsEvent

class EventAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]
    
class EventAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]

    readonly_fields = ('comments',)

    def comments(self, obj):
        return obj.comments_event_set.all()


# start of product sector
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

class CommentsInline(admin.TabularInline):
    model = CommentsProduct
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]
    
class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ('comments',)  

    def comments(self, obj):
       return obj.commentsproduct_set.all()