from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.

def home(request): return render(request, 'pages/index.html')

def getPassword(request): return render(request, 'pages/getpassword.html')

def password(request):
    lenght = int(request.GET.get('length'))
    characters = list(string.ascii_lowercase)

    if (request.GET.get('uppercase')):
        print('uppercase')
        characters.extend(list(string.ascii_uppercase))

    if (request.GET.get('numbers')):
        print('numbers')
        characters.extend(list(string.digits))
    
    if (request.GET.get('special')):
        print('special')
        characters.extend(list(string.punctuation))

    randompassword = [str(random.choice(characters)) for _ in range(lenght)]

    return render(request, 'pages/password.html', { 'password': ''.join(randompassword) })
