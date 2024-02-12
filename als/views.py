from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm


def loginPage(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        alsUser = authenticate(request, username=username, password=password)
        if alsUser is not None:
            login(request, alsUser)
            return redirect('dashboard')
        
    return render(request, 'als/login.html')

def logoutUser(request) :
    logout(request)
    return redirect('login')

def registerPage(request) :
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'als/register.html', context)

def dashboard(request) :
    return render(request, 'als/dashboard.html')