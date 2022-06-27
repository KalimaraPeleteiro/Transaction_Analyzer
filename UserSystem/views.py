from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

from random import randint
from UserSystem.email import send_email


# Create your views here.
def login(request):
    return render(request, 'login.html')


def enter(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password = password

        if email == "" or password == "":
            print("Campos Vazios!")
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return render(request, 'dashboard.html')
            else:
                print("Senha Errada!")
                return redirect('login')
        else:
            print("Usuário não cadastrado!")
            return redirect('signup')


    return render(request, 'login.html')


def register(request):
    if request.method == "GET":
        username = request.GET["user"]
        email = request.GET['email']

        if User.objects.filter(email=email).exists():
            print("Usuário já existe!")
            return render(request, 'signup.html')
        else:
            password = f'{randint(1, 999999)}'

            send_email(email, password, username)

            new_user = User.objects.create(username = username, email = email)
            new_user.set_password(password)
            new_user.save()

    return redirect('login')


def signup(request):
    return render(request, 'signup.html')
