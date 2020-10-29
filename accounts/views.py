from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def events(request):
    return render(request, 'accounts/events.html')

def people(request):
    return render(request, 'accounts/people.html')

def search(request):
    return render(request, 'accounts/search.html')
