from django import forms

class CustomerForm(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=50)