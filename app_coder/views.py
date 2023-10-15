from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse, HttpRequest
from app_coder.models import Customer
from app_coder.forms import CustomerForm, SearchForm

# Create your views here.

def inicio(request):
    
    formulario = CustomerForm()
    
    if request.method == 'POST':
        
        formulario = CustomerForm(request.POST)
        
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            cliente = Customer(name=data['name'], description=data['description'])
            
            cliente.save()
            
            return redirect('customer')
        
        else:
            
            return render(request, 'app_coder\inicio.html', {'formulario': formulario})
        
    return render(request, 'app_coder\inicio.html', {'formulario': formulario})

def create_customer(request):
    
    if request.method == 'POST':
        
        formulario = request.POST
               
        formulario1 = formulario.get('name')
        
        cliente = Customer.objects.filter(name=formulario1)
        
        cliente_search = cliente.first()
        
        return render(request, "app_coder/customer.html", {'formulario': cliente, 'cliente': cliente_search})
    
    else:
            
        return render(request, 'app_coder/customer.html', {})
    
    # else:
        
    # return render(request, 'app_coder/customer.html', {})

    # formulario = Customer.objects.filter()
    
    # if request.method == 'POST':
        
    #     if  request.POST.get('name'):
            
    #         for name in Customer.objects.all():
                
    #             if  request.POST.get('name'):
                    
    #                 return Customer.objects.get('name')
                
    # return render(request, 'app_coder/customer.html' , {'formulario': formulario})                    
        
    #     # formulario = CustomerForm(request.POST)
        
        # if formulario.is_valid():
            
        #     data = formulario.cleaned_data
            
        #     cliente = Customer(name=data['name'], description=data['description'])
            
        #     cliente.save()
            
        #     return redirect('customer')
    
    # if request.method == 'POST':

    #   if  request.POST.get('name'):
          
    #         t = request.POST('name')
            
    #         s = Customer.objects.filter(name=str(t))
            
    #         return render(request, 'app_coder/customer.html' , {'formulario': formulario})

    #   else: 
    #       return render(request, 'app_coder/customer.html' , {'formulario': formulario})
      
    #     pass
            # respuesta = "No se enviaron los datos"
            # respuesta1 = render(request, "AppCoder/inicio.html", {"respuesta":respuesta})
            # return respuesta1
    # if request.method == 'POST':
    
    #     formulario = CustomerForm(request.POST)
    
    #     if formulario.is_valid():
    #         data = formulario.cleaned_data
    #         cliente = Customer(name=data.get('name', description= data['description'])
    #         cliente.save()
    #         return redirect('customer')
    #     else:
    #         return render(request, 'app_coder\customer.html', {'formulario': formulario})
            
    # formulario = CustomerForm()
    
    # return render(request, 'app_coder\customer.html', {'formulario': formulario})
    
    # if request.method == 'POST':
        
    #     formulario = CustomerForm(request.POST)
        
    #     if formulario.is_valid():
            
    #         data = formulario.cleaned_data
            
    #         cliente = Customer(name=data.get('nombre'), description=data['descripción'])
            
    #         cliente.save()
            
    #     formulario = CustomerForm()
        
    #     return render(request, 'app_coder/customer.html', {'formulario':formulario})