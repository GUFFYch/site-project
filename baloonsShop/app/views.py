from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth import logout, authenticate, login
from .models import *
from datetime import datetime, date
from django.contrib.contenttypes.models import ContentType



def index(request):
    content = {}
    for i in SiteSettings.objects.filter(id = 1):    
        content['main'] = {
            'name': i.name,
            'logo': i.logoImage.url.replace('app/', ''),
            'descriptionImage': i.descriptionmImage.url.replace('app/', ''),
            'descriptionText': i.descriptionText,
            'images': [j.image.url.replace('app/', '') for j in i.coruselimage_set.filter(post_id = i.id)]
            }
    content['events'] = [{
        'name':i.name,
        'id': i.id,
        'content_type':ContentType.objects.get_for_model(i).model,
        } for i in Event.objects.all()]
    content['products'] = [{
        'content_type': ContentType.objects.get_for_model(product).model,
        'id': product.id,
        'name': product.name,
        'link': product.name.replace(' ', '-').replace('"', ''),
        'explanation': product.explanation,
        'price': product.price,
        'mainImage': product.mainImage.url.replace('/app/', ''),
        'images': [i.image.url for i in product.productimage_set.filter(post_id = product.id)],
        'events': [{
            'content_type': ContentType.objects.get_for_model(i).model,
            'name': i.name,
            'link': i.name.replace(' ', '-').replace('"', '')
            } for i in Event.objects.filter(product__id = product.id)]
        } for product in Product.objects.all()]
    
    if request.method == 'POST':
        item_type = request.POST['item'].split('|')[-1]
        item_id = int(request.POST['item'].split('|')[0])

        if item_type == 'event':
            item = Event.objects.get(pk=item_id)
        elif item_type == 'product':
            item = Product.objects.get(pk=item_id)
        else:
            item = None
        
        if item:
            Request.objects.create(
                name=request.POST['name'],
                contact=request.POST['phone'],
                event=item if isinstance(item, Event) else None,
                product=item if isinstance(item, Product) else None,
            )
        return HttpResponseRedirect('/')
    
        
    return render(request, 'index.html', content)

def eventPage(request, event_name):
    event_name = event_name.replace('%20', ' ')
    content = {}
    for i in SiteSettings.objects.filter(id = 1):    
        content['main'] = {
            'name': i.name,
            'logo': i.logoImage.url.replace('/app/', '../'),
            'descriptionImage': i.descriptionmImage,
            'descriptionText': i.descriptionText,
            'images': [j.image.url for j in i.coruselimage_set.filter(post_id = i.id)]
            }
        
    content['all_events'] = [{
        'content_type': ContentType.objects.get_for_model(event).model,
        'name':event.name,
        'id': event.id,
        'content_type':ContentType.objects.get_for_model(event).model,
        } for event in Event.objects.all()]
    
    content['all_products'] = [{
        'content_type': ContentType.objects.get_for_model(product).model,
        'name':product.name,
        'id': product.id,
        'content_type':ContentType.objects.get_for_model(product).model,
        } for product in Product.objects.all()]
    
    content['events'] = [{
        'content_type': ContentType.objects.get_for_model(event).model,
        'name': event.name,
        'explanation': event.explanation,
        'price': event.price,
        'mainImage': event.mainImage.url.replace('/app/', '../'),
        'images': [i.image.url.replace('/app/', '../') for i in event.eventimage_set.filter(post_id = event.id)],
        'products': [{
            'content_type': ContentType.objects.get_for_model(product).model,
            'name': product.name,
            'link': product.name.replace(' ', '-').replace('"', ''),
            'explanation': product.explanation,
            'price': product.price,
            'mainImage': product.mainImage.url.replace('/app/', '../'),
            'images': [i.image.url.replace('/app/', '../') for i in product.productimage_set.filter(post_id = product.id)]}
            for product in Product.objects.filter(event_id = event.id)],
        } for event in Event.objects.filter(name = event_name)]
    
    if request.method == 'POST':
        item_type = request.POST['item'].split('|')[-1]
        item_id = int(request.POST['item'].split('|')[0])

        if item_type == 'event':
            item = Event.objects.get(pk=item_id)
        elif item_type == 'product':
            item = Product.objects.get(pk=item_id)
        else:
            item = None
        
        if item:
            Request.objects.create(
                name=request.POST['name'],
                contact=request.POST['phone'],
                event=item if isinstance(item, Event) else None,
                product=item if isinstance(item, Product) else None,
            )
        return HttpResponseRedirect('/')
    
    return render(request, 'event.html', content)
