from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


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
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    conn.commit()
    conn.close()
    return HttpResponse('Hello from Python!');

def sss(request):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    v='aaaaa'
    cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
       v = row[0];
    conn.close()
    return HttpResponse(v);


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

