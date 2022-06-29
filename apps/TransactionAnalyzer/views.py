from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from TransactionAnalyzer.file_operations import handle_uploaded_file
from TransactionAnalyzer.forms import CSVForm
from TransactionAnalyzer.models import MoneyOperation


# Rotas de Arquivos HTML
def dashboard(request):
    """ 
    Página Principal da Plataforma. As operações consideradas "suspeitas" são enviadas
    por essa função, sendo, no momento, classificadas como quaisquer operações acima de
    10000 reais.
    """
    
    if request.user.is_authenticated:
        operations = MoneyOperation.objects.all().filter(usuario = request.user.id)
        suspicious_operations = []

        for operation in operations:
            if operation.valor > 10000:
                suspicious_operations.append(operation)
        
        context = {
            'suspicious': suspicious_operations,
            'suspicious_length': len(suspicious_operations),
            'valid_operations': len(operations) - len(suspicious_operations),
            'operations_number': len(operations),
            'username': User.get_username(request.user)
        }

        return render(request, 'TransactionAnalyzer/dashboard.html', context=context)
    else:
        return redirect('login')


def upload(request):
    if request.user.is_authenticated:
        return render(request, 'TransactionAnalyzer/import.html', {'form': CSVForm()})
    else:
        return redirect('login')


def history(request):
    if request.user.is_authenticated:
        operations = MoneyOperation.objects.all().filter(usuario = request.user.id)
        return render(request, 'TransactionAnalyzer/transactions.html', {'operations': operations})    
    else:
        return redirect('login')


# Rotas Intermediárias (Que Realizam Certas Ações)
def newfile(request):
    if request.method == "POST":
        user = get_object_or_404(User, pk = request.user.id)       
        handle_uploaded_file(request.FILES['file_upload'], user)

    return render(request, 'TransactionAnalyzer/import.html', {'form': CSVForm()})


def operation(request, operation_id):
    operation = get_object_or_404(MoneyOperation, pk=operation_id)

    return render(request, "TransactionAnalyzer/operation.html", {'operation': operation})


def logout(request):
    auth.logout(request)
    return redirect('login')
