from django.shortcuts import redirect, render
from django.contrib.auth.models import User

import bcrypt
from random import randint
from UserSystem.email import send_email


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == "GET":
        username = request.GET["user"]
        email = request.GET['email']

        if User.objects.filter(email=email).exists():
            print("Usuário já existe!")
            return render(request, 'signup.html')
        else:
            password = f'{randint(1, 999999)}'.encode(encoding='utf-8')

            # https://zetcode.com/python/bcrypt/
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(password, salt)

            send_email(email, password, username)

            new_user = User.objects.create(username = username, email = email,
                                           password = hash)
            new_user.save()

    return redirect('login')


def signup(request):
    return render(request, 'signup.html')
