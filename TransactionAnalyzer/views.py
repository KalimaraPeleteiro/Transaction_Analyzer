from django.shortcuts import render

from TransactionAnalyzer.forms import CSVForm
from csv import reader
from io import TextIOWrapper


def dashboard(request):
    return render(request, 'dashboard.html')


def upload(request):
    form = CSVForm()
    context = {'form': form}
    return render(request, 'import.html', context)


def newfile(request):
    if request.method == "POST":
        
        # Convertendo o arquivo para texto antes de ler o csv
        file = request.FILES['file_upload']
        file = TextIOWrapper(file, encoding='utf-8')
        file = reader(file)

        for line in file:
            print(line)

    return render(request, 'import.html')


def history(request):
    return render(request, 'transactions.html')


def profile(request):
    return render(request, 'profile.html')