from django.shortcuts import render

from TransactionAnalyzer.forms import CSVForm
from csv import reader
from io import TextIOWrapper


def dashboard(request):
    return render(request, 'dashboard.html')


def upload(request):
    return render(request, 'import.html', {'form': CSVForm()})


def newfile(request):
    if request.method == "POST":
        
        # Convertendo o arquivo para texto antes de ler o csv
        file = request.FILES['file_upload']
        file = TextIOWrapper(file, encoding='utf-8')
        file = reader(file)

        for line in file:
            print(f'Banco (Origem) = {line[0]}')
            print(f'Agencia (Origem) = {line[1]}')
            print(f'Conta (Origem) = {line[2]}')
            print(f'Banco (Destino) = {line[3]}')
            print(f'Agencia (Destino) = {line[4]}')
            print(f'Conta (Destino) = {line[5]}')
            print(f'Valor = {line[6]}')
            print(f'Data = {line[7]}')
            print('\n')


    return render(request, 'import.html', {'form': CSVForm()})


def history(request):
    return render(request, 'transactions.html')


def profile(request):
    return render(request, 'profile.html')