import re
from .models import *
from django.shortcuts import render
from datetime import datetime, date
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth import logout, authenticate, login
from django.contrib.contenttypes.models import ContentType

def sized_render(request, file_name, content):
    
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return render(request, f'mobile/{file_name}', content)
    else:
        return render(request, file_name, content)

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
        'link':i.name.replace(' ', '-').replace('"', ''),
        'id': i.id,
        } for i in Event.objects.all()]
    content['products'] = [{
        'content_type': ContentType.objects.get_for_model(product).model,
        'id': product.id,
        'name': product.name,
        'link': product.name.replace(' ', '-').replace('"', ''),
        'explanation': product.explanation,
        'price': product.price,
        'mainImage': product.mainImage.url.replace('/app/', ''),
        'rate_sum': product.rate_sum,
        'vote_sum': product.vote_sum,
        'rating': product.rating,
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
    
        
    return sized_render(request, 'index.html', content)

def eventPage(request, event_name):
    org_event_name, event_name = event_name, event_name.replace(' ', '"').replace('-', ' ')
    content = {}
    for i in SiteSettings.objects.filter(id = 1):    
        content['main'] = {
            'name': i.name,
            'logo': i.logoImage.url.replace('/app/', '../../'),
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
    
    content['event'] = [{
        'content_type': ContentType.objects.get_for_model(event).model,
        'name': event.name,
        'explanation': event.explanation,
        'price': event.price,
        'mainImage': event.mainImage.url.replace('/app/', '../../'),
        'rate_sum': event.rate_sum,
        'vote_sum': event.vote_sum,
        'rating': event.rating,
        'images': [{'url': i.image.url.replace('/app/', '../../'), 'id':i.id} for i in event.eventimage_set.filter(post_id = event.id)],
        'products': [{
            'content_type': ContentType.objects.get_for_model(product).model,
            'name': product.name,
            'link': product.name.replace(' ', '-').replace('"', ''),
            'explanation': product.explanation,
            'price': product.price,
            'mainImage': product.mainImage.url.replace('/app/', '../../'),
            'rate_sum': product.rate_sum,
            'vote_sum': product.vote_sum,
            'rating': product.rating,
            'images': [i.image.url.replace('/app/', '../../') for i in product.productimage_set.filter(post_id = product.id)]}
            for product in Product.objects.filter(event_id = event.id)],
        'comments': [comment for comment in CommentsEvent.objects.filter(event = event)]
        } for event in Event.objects.filter(name = event_name)]
    
    if request.method == 'POST' and 'requestButton' in request.POST:
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
        return HttpResponseRedirect(f'event/{org_event_name}/')
    
    if request.method == 'POST' and 'CommentEventBtn' in request.POST:
        event = Event.objects.get(name = event_name)
        comment = CommentsEvent()
        comment.comentator = request.POST['name']
        comment.event = event
        comment.review = request.POST['review']
        comment.rating = request.POST.get('rating', '0')
        event.rate_sum = event.rate_sum + 1
        event.vote_sum = event.vote_sum + int(request.POST.get('rating', '0'))
        event.rating = round((event.vote_sum + int(request.POST.get('rating', '0')))/(event.rate_sum + 1), 1)
        comment.save()
        event.save()
        return HttpResponseRedirect(f'event/{org_event_name}/')
    
    return sized_render(request, 'event.html', content)



def productPage(request, product_name):
    org_product_name, product_name = product_name, product_name.replace(' ', '"').replace('-', ' ')
    content = {}
    for i in SiteSettings.objects.filter(id = 1):    
        content['main'] = {
            'name': i.name,
            'logo': i.logoImage.url.replace('/app/', '../../'),
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
    
    content['product'] = [{
        'content_type': ContentType.objects.get_for_model(product).model,
        'name': product.name,
        'explanation': product.explanation,
        'price': product.price,
        'mainImage': product.mainImage.url.replace('/app/', '../../'),
        'rate_sum': product.rate_sum,
        'vote_sum': product.vote_sum,
        'rating': product.rating,
        'images': [{'url': i.image.url.replace('/app/', '../../'), 'id':i.id} for i in product.productimage_set.filter(post_id = product.id)],
        'events': [{
            'content_type': ContentType.objects.get_for_model(i).model,
            'name': i.name,
            'link': i.name.replace(' ', '-').replace('"', '')
            } for i in Event.objects.filter(product__id = product.id)],
        'comments': [comment for comment in CommentsProduct.objects.filter(product = product)]
        } for product in Product.objects.filter(name = product_name)]
    
    if request.method == 'POST' and 'requestButton' in request.POST:
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
                product=item if isinstance(item, product) else None,
            )
        return HttpResponseRedirect(f'product/{org_product_name}/')
    
    if request.method == 'POST' and 'CommentproductBtn' in request.POST:
        product = Product.objects.get(name = product_name)
        comment = CommentsProduct()
        comment.comentator = request.POST['name']
        comment.product = product
        comment.review = request.POST['review']
        comment.rating = request.POST.get('rating', '0')
        product.rate_sum = product.rate_sum + 1
        product.vote_sum = product.vote_sum + int(request.POST.get('rating', '0'))
        product.rating = round((product.vote_sum + int(request.POST.get('rating', '0')))/(product.rate_sum + 1), 1)
        comment.save()
        product.save()
        return HttpResponseRedirect(f'product/{org_product_name}/')
    
    return sized_render(request, 'product.html', content)