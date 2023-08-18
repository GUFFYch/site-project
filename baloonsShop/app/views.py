from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth import logout, authenticate, login
from .models import *
from datetime import datetime, date


def index(request):
    return render(request, 'index.html')