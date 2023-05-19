from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'auth/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
           messages.error(request, "Passwords don't match")
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.save()

        messages.success(request, "SignUp succesful! Login to continue")

        return redirect('login')    
    return render(request, 'auth/signup.html')

def signout(request):
    logout(request)
    messages.success(request, "SignOut succesful!")
    return redirect('login')
