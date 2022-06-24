from django.shortcuts import render
from TransactionAnalyzer.file_operations import handle_uploaded_file

from TransactionAnalyzer.forms import CSVForm


def dashboard(request):
    return render(request, 'dashboard.html')


def upload(request):
    return render(request, 'import.html', {'form': CSVForm()})


def newfile(request):
    if request.method == "POST":        
        handle_uploaded_file(request.FILES['file_upload'])



    return render(request, 'import.html', {'form': CSVForm()})


def history(request):
    return render(request, 'transactions.html')


def profile(request):
    return render(request, 'profile.html')