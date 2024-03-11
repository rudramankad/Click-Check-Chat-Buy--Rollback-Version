from django.shortcuts import render, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def QuestLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('index:index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('accounts:QuestLogin')
        
    else:
        return render(request, 'QuestLogin.html')


def QuestRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, 'You have successfully registered.')
        # login(request, user)
        return redirect('accounts:QuestLogin')
    else:
        return render(request, 'QuestRegister.html')


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Send email with reset password link
        messages.success(request, 'An email has been sent to reset your password.')
        return redirect('accounts:QuestLogin')
    else:
        messages.success(request, 'An email has been sent to reset your password.')
        return render(request, 'forgotpassword.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('index:index')