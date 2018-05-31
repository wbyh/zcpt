from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from django.views.decorators.csrf import csrf_exempt

import sqlite3


# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def aaa(request):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           INT    NOT NULL,
           AGE            INT     NOT NULL);''')
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE) VALUES (1, 1, 32 )");
    conn.commit()
    conn.close()
    return HttpResponse('Hello from Python!');

@csrf_exempt
def sss(request):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("UPDATE COMPANY set NAME=" + request.POST.get('n') + ",AGE=" + request.POST.get('t') + " where ID=1")
    conn.commit()
    conn.close()
    return HttpResponse(request.POST.get('n',None) + '  ' + request.POST.get('t',None));

@csrf_exempt
def ccc(request):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor = c.execute("SELECT ID,NAME,AGE from COMPANY")
    n=0
    t=0
    for row in cursor:
        n = row[1]
        t = row[2]
    conn.close()
    return HttpResponse(n + '-----' + t);

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

