from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm


def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            login(request, user) 
            messages.success(request, f' welcome {username} !!') 
            return redirect('book-list') 
        else: 
            messages.info(request, f'account does not exit plz sign in') 
    form = LoginForm()
    ctx = {"form":form}
    return render(request,'login.html',ctx)


def logout_user(request):
    logout(request)
    return redirect('login')
