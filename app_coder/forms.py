from django import forms

class CustomerForm(forms.Form):
    #Especificar los campos
    name = forms.CharField(max_length=30)
    description = forms.CharField(max_length=50)