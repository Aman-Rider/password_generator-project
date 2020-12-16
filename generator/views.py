from django.shortcuts import render
from django.http import HttpResponse
from django.utils.crypto import get_random_string
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvqxyz')
    thepassword = ''
    if request.POST.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.POST.get('specialchar'):
        characters.extend(list('!@#$%^&*()'))
    if request.POST.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.POST.get('length', 10))
    thepassword = get_random_string(length, characters)
    # for x in range(length):
    #     thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {"password":thepassword})

def aboutus(request):
    return render(request,'generator/aboutus.html')