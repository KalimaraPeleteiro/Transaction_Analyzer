from django import forms


class CSVForm(forms.Form):
    file_upload = forms.FileField(label='Insira seu arquivo CSV')
    