from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


import sqlite3


# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def sss(request):
    conn = sqlite3.connect('test.db')
    return HttpResponse('Hello from Python!');


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

