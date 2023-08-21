from django.shortcuts import render, redirect
# Django Authentications
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Model Names
from .models import Room, Message, Topic
#Forms Models
from .forms import RoomForm
#Query Model
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib import messages

def loginuser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.info(request, "USer not Found in the Database")

        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('home')
    
    context = {
        'page':page
    }
    return render(request, 'loginsignup.html', context)


def signupuser(request):
    page = 'signup'
    if request.user.is_authenticated:
        return redirect('home')
    
    context = {
        'page':page
    }

    return render(request, 'loginsignup.html', context)

def logoutuser(request):
    logout(request)
    return redirect('loginuser')

@login_required(login_url='loginuser')
def home(request):
    page = "home"
    
    q = request.GET.get('q')

    if request.GET.get('q'):
        q=request.GET.get('q')
    else:
        q=""

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q) 
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {
        'page':page,
        'rooms':rooms,
        'topics':topics,
        'room_count':room_count,
    }
    return render(request, 'studybuddy/home.html', context)


def room(request, pk):
    page = 'room'
    room = Room.objects.get(id=pk)
    

    context = {
        'page':page,
        'room':room,
    }
    return render(request, 'studybuddy/room.html', context)

def createRoom(request):
    page = "create-room"
    form = RoomForm
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'page':page,
        'form':form
    }
    return render(request, 'studybuddy/room_form.html', context)



def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'studybuddy/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    
    context = {
        'obj':room
    }
    return render(request,'delete.html', context)