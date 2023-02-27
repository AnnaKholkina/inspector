from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from cad.models import Unit, Member


def main_cad(request):
    if not request.user.is_authenticated:
        return redirect('/signin')

    query_results = Unit.objects.all()
    return render(request, "cad/main.html", context={'query_results': query_results})

def add_unit(request):
    if request.method == 'POST':
        unit_name = request.POST['unit_name']
        status = request.POST['status']
        unit_table = Unit(unit_name=unit_name, status=status)
        unit_table.save()
    return render(request, "cad/main.html")

def change_status(request, username, status):
    member_in_unit = Member.objects.get(name=username).unit_name
    units = Unit.objects.get(unit_name=member_in_unit)
    units.status = status
    units.save()
    return render(request, "cad/main.html")

def add_member(request):
    if request.method == 'POST':
        unit_name = request.POST['unit_name']
        username = request.POST['username']
        members = Member(unit_name=unit_name, name=username)
        members.save()
    return render(request, "cad/main.html")

def logout_user(request):
    logout(request)
    return redirect('/signin')
