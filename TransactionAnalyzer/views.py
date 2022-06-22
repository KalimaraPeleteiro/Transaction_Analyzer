from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')


def upload(request):
    return render(request, 'import.html')


def history(request):
    return render(request, 'transactions.html')


def profile(request):
    return render(request, 'profile.html')