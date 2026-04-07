from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')


def room(request, room):
    if not request.user.is_authenticated:
        return redirect('/login/')

    room_details = get_object_or_404(Room, name=room)

    return render(request, 'room.html', {
        'username': request.user.username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    room, created = Room.objects.get_or_create(name=room_name)

    return redirect(f'/{room_name}/?username={username}')


def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_name = request.POST.get('room_name')

        room = get_object_or_404(Room, name=room_name)

        Message.objects.create(
            value=message,
            user=username,
            room=room
        )

        return HttpResponse('Message sent successfully')

    return HttpResponse('Invalid request', status=400)


def getMessages(request, room):
    room_obj = get_object_or_404(Room, name=room)

    messages = Message.objects.filter(room=room_obj).order_by('date')

    return JsonResponse({
        "messages": [
            {
                "value": msg.value,
                "user": msg.user,
                "date": msg.date.strftime("%H:%M")
            }
            for msg in messages
        ]
    })

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "User already exists"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect('/')

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('/login/')