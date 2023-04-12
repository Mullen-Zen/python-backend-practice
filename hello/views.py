import re
from django.http import HttpResponse
from django.utils.timezone import datetime
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    return render(
        request,
        'hello/hellothere.html',
        {
        'name': name,
        'date': datetime.now()
        }
    )