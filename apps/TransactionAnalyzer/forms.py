from django import forms


# Formulário do Input do arquivo CSV
class CSVForm(forms.Form):
    file_upload = forms.FileField(label='Insira seu arquivo CSV')
    