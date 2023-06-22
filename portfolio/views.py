from django.http import HttpResponse
from django.shortcuts import render
from rabees.models import Userdata
from . import views
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    u = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        usermessage = request.POST.get('usermessage')
        data = Userdata(username=username, useremail=useremail,
                        usermessage=usermessage)
    data.save()
    print(data)
    User_data = {
        'username': username,
        'useremail': useremail,
        'usermessage': usermessage,
    }
    with open('Userdata.json', 'a') as u:
        json.dump(User_data, u, indent=4)
    u = "Congratulations! Now you are our member👻"
    return render(request, 'home.html', {
        'u': u,
        'username': username,
        'useremail': useremail,
        'usermessage': usermessage
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
