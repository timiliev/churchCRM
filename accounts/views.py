from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

# Create your views here.
from accounts.models import *

def home(request):
    return render(request, 'accounts/home.html')

def events(request):
    return render(request, 'accounts/events.html')

def people(request):
    members = Member.objects.all()
    return render(request, 'accounts/people.html', {'members': members})

def search(request):
    return render(request, 'accounts/search.html')
