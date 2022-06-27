from django.shortcuts import redirect, render
from django.contrib import auth

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
        handle_uploaded_file(request.FILES['file_upload'])

    return render(request, 'import.html', {'form': CSVForm()})


def history(request):
    if request.user.is_authenticated:
        operations = MoneyOperation.objects.all()
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