from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth import logout, authenticate, login
from .models import *
from datetime import datetime, date


def index(request):
    content = {}
    content['events'] = Event.objects.all()
    content['products'] = [{
        'name': product.name,
        'explanation': product.explanation,
        'price': product.price,
        'mainImage': product.mainImage.url.replace('/app/', ''),
        'images': [i.image.url for i in product.productimage_set.filter(post_id = product.id)],
        'events': [{
            'name': i.name,
            'mainImage': i.mainImage.url.replace('/app/', ''),                
            } for i in Event.objects.filter(product__id = product.id)]
        } for product in Product.objects.all()]
    return render(request, 'index.html', content)

def eventPage(request, event_name):
    content = {}
    content['events'] = [{
        'name': event.name,
        'explanation': event.explanation,
        'price': event.price,
        'mainImage': event.mainImage.url.replace('/app/', ''),
        'images': [i.image.url for i in event.eventimage_set.filter(post_id = event.id)],
        'products': [{
            'name': product.name,
            'explanation': product.explanation,
            'price': product.price,
            'mainImage': product.mainImage.url.replace('/app/', ''),
            'images': [i.image.url for i in product.productimage_set.filter(post_id = product.id)]}
            for product in Product.objects.filter(event_id = event.id)],
        } for event in Event.objects.filter(name = event_name)]
    return render(request, 'event.html', content)
