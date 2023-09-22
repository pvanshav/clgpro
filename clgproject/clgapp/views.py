
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.

def home(request):
    return render(request, 'index.html')
def form(request):
    return render(request, 'form.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('form.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login.html')

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['Password']
        password1 = request.POST['Cpassword']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exist")
                return redirect('login.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email exist")
                return redirect('register.html')
            else:
                user1 = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email, password=password)
                user1.save();
                print("User created")
                return redirect('login.html')
        else:
            messages.info(request,"Password not matching")
            return redirect('register.html')
        return redirect('/')
    return render(request,'register.html')