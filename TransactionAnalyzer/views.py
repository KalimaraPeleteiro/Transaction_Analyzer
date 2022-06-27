from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

from TransactionAnalyzer.file_operations import handle_uploaded_file
from TransactionAnalyzer.forms import CSVForm
from TransactionAnalyzer.models import MoneyOperation


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


def upload(request):
    if request.user.is_authenticated:
        return render(request, 'import.html', {'form': CSVForm()})
    else:
        return render(request, 'login.html')


def newfile(request):
    if request.method == "POST":
        user = get_object_or_404(User, pk = request.user.id)       
        handle_uploaded_file(request.FILES['file_upload'], user)

    return render(request, 'import.html', {'form': CSVForm()})


def history(request):
    if request.user.is_authenticated:
        operations = MoneyOperation.objects.all().filter(usuario = request.user.id)
        return render(request, 'transactions.html', {'operations': operations})    
    else:
        return render(request, 'login.html')
    

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def operation(request, operation_id):
    operation = get_object_or_404(MoneyOperation, pk=operation_id)

    return render(request, "operation.html", {'operation': operation})