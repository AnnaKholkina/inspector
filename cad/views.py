from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from cad.models import Unit

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

def change_status_10_6(request):
    if request.method == 'POST':
        Unit.objects.filter(unit_name=request.POST['unit_name']).update(status='10-6')
    return render(request, "cad/main.html")

def change_status_10_8(request):
    if request.method == 'POST':
        Unit.objects.filter(unit_name=request.POST['unit_name']).update(status='10-8')
    return render(request, "cad/main.html")

def add_member(request):
    pass

def logout_user(request):
    logout(request)
    return redirect('/signin')
