from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

from random import randint
from UserSystem.email import send_email


# Rotas de Arquivo HTML.
def login(request):
    return render(request, 'UserSystem/login.html')


def signup(request):
    return render(request, 'UserSystem/signup.html')


# Rotas Intermediárias (Que Realizam Alguma Ação)
def enter(request):
    """
    Rota de Login. São realizadas três verificações, e, caso o usuário passe por elas,
    ele pode acessar a plataforma.
    """

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Verificação 01 - Algum Campo Está Vazio?
        if email == "" or password == "":
            return redirect('login')
        
        # Verificação 02 - O Usuário está cadastado?
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)

            # Verificação 03 - As credenciais são válidas?
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')
        else:
            return redirect('signup')


    return render(request, 'UserSystem/login.html')


def register(request):
    """
    Rota de registro de um novo usuário. Após verificar se o usuário já existe, uma senha é criada
    com um número aleatório de 6 dígitos, encriptografada pelo django e enviada ao usuário por email.
    """

    if request.method == "GET":
        username = request.GET["user"]
        email = request.GET['email']

        # Verificação 01 - O Usuário já existe?
        if User.objects.filter(email=email).exists():
            return redirect('signup')
        else:
            password = f'{randint(1, 999999)}'

            send_email(email, password, username)

            new_user = User.objects.create(username = username, email = email)

            # O Bcrypt é aplicado aqui pelo Django.
            new_user.set_password(password)

            new_user.save()

    return redirect('login')
