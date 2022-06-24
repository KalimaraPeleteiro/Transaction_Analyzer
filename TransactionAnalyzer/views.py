from django.shortcuts import render

from TransactionAnalyzer.file_operations import handle_uploaded_file
from TransactionAnalyzer.forms import CSVForm
from TransactionAnalyzer.models import MoneyOperation


def dashboard(request):
    return render(request, 'dashboard.html')


def upload(request):
    return render(request, 'import.html', {'form': CSVForm()})


def newfile(request):
    if request.method == "POST":        
        handle_uploaded_file(request.FILES['file_upload'])



    return render(request, 'import.html', {'form': CSVForm()})


def history(request):
    operations = MoneyOperation.objects.all()

    return render(request, 'transactions.html', {'operations': operations})


def profile(request):
    return render(request, 'profile.html')