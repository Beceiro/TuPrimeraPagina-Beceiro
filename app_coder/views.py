from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse, HttpRequest
from app_coder.models import Customer
from app_coder.forms import CustomerForm

# Create your views here.

def inicio(request):
        
    return render(request, 'app_coder/inicio.html')

def create_customer(request):
    
    if request.method == 'POST':
        formulario = CustomerForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Customer(name=data.get('nombre'), description= data['descripción'])
            cliente.save()
            return redirect('customer')
        else:
            return render(request, 'app_coder\customer.html', {'formulario': formulario})
            
    formulario = CustomerForm()
    return render(request, 'app_coder\customer.html', {'formulario': formulario})
    
    # if request.method == 'POST':
        
    #     formulario = CustomerForm(request.POST)
        
    #     if formulario.is_valid():
            
    #         data = formulario.cleaned_data
            
    #         cliente = Customer(name=data.get('nombre'), description=data['descripción'])
            
    #         cliente.save()
            
    #     formulario = CustomerForm()
        
    #     return render(request, 'app_coder/customer.html', {'formulario':formulario})