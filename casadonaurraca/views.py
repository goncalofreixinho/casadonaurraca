from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse


# Create your views here.

def index(request):
    params = {
        'title': 'Home Page',
    }
    return render(request, 'index.html')


def about(request):
    params = {
        'title': 'About',
    }
    return render(request, 'about-us.html')

def contact(request):
    params = {
        'title': 'Contactos',
    }
    return render(request, 'contact.html')

def rooms(request):
    params = {
        'title': 'Contact Page',
    }
    return render(request, 'rooms.html')
