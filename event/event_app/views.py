from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
    events = event_info.objects.all()
    user = request.user

    return render(request, 'event/index.html', {
        'events' : events,
        'user' : user
    })

def create_event(request):
    if request.method == "POST":
        event_details = request.POST['event_details']
        Location_details = request.POST['Location_details']
        Contact_details = request.POST['Contact_details']
        
        host_user = request.user
        obj = event_info()
        obj.Host_name = host_user
        obj.Event_details = event_details
        obj.Location = Location_details
        obj.Contact_details = Contact_details
        obj.save()

        return redirect('event:home')
    return render(request, 'event/create_event.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, "password do not match")
            return redirect('event:signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('event:signup')

        myuser = User.objects.create_user(username=username, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, 'Your account is created')
        return redirect('event:signin')

    return render(request, 'event/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)

            return redirect('event:home')
        
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'event/signin.html')

def update_event(request, id):
    event = event_info.objects.get(pk=id)

    if request.method == "POST":
        event_details = request.POST['event_details']
        location_details = request.POST['location_details']
        contact_details = request.POST['contact_details']

        event.Event_details = event_details
        event.Location = location_details
        event.Contact_details = contact_details
        event.save()

        return redirect('event:home')

    return render(request, 'event/update_event.html', {
        'event' : event
    })

def delete_event(request, id):
    event = event_info.objects.get(pk=id)
    event.delete()

    return redirect('event:home')
    