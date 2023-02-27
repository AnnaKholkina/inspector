from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from inspector import settings


def home(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST["pass1"]

        myuser = User.objects.create_user(username=username, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        return redirect('signin')

    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            request.session['fname'] = fname
            request.session['username'] = username
            return redirect('/cad/')
        else:
            messages.error(request, "Bad Credentials!!")
            return render(request, "accounts/signin.html")

    return render(request, "accounts/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

