from django.shortcuts import render,redirect 
from .models import persona
from .models import tipodocumento
from .models import ciudad
from .forms import PersonaForm
from .forms import CiudadForm

def index(request):
    return render(request,'inicio.html')






def inicio(request):
    personas=persona.objects.all()
    info={
        'personas':personas
    }
    return render(request,'index.html',info)


def crear(request):
    if request.method=='GET':
        formu=PersonaForm()
        info={
            'formu':formu
            }
    else:
        formu=PersonaForm(request.POST)
        info={
            'formu':formu
            }
        if formu.is_valid():
            formu.save()
        return redirect('inicio')
                       
    return render(request,'registro.html',info)

def editar_persona(request,id):
    pers=persona.objects.get(id = id)
    if request.method=='GET':
        formu=PersonaForm(instance=pers)
        contexto={
            'formu':formu
        }
    else:
        
        formu=PersonaForm(request.POST,instance=pers)
        contexto={
            'formu':formu
        }   
        if formu.is_valid():
            formu.save()
            return redirect('inicio')
           
        return render(request,'registro.html',contexto)
    


    return render(request,'registro.html',contexto)        

def eliminar_persona(request,id):
    pers=persona.objects.get(id = id)
    pers.delete()
    return redirect('inicio')

#ciudad

def readCiudad(request):
    ciudades=ciudad.objects.all()
    contexto={
        'ciudades':ciudades
    }
    return render(request,'ciudades.html',contexto)

def crearCiudad(request):
    if request.method=='GET':
        formula=CiudadForm()
        contexto={
            'formula':formula
        }
        
    else:
        formula=CiudadForm(request.POST)
        contexto={
            'formula':formula
        }
        if formula.is_valid():
            formula.save()
        return redirect('readciudad')
    return render(request,'Ciudadregitro.html',contexto) 


def editarciudad(request,id):
    ciu=ciudad.objects.get(id = id)
    if request.method=='GET':
        formu=CiudadForm(instance=pers)
        contexto={
            'formu':formu
        }
    else:
        
        formu=CiudadForm(request.POST,instance=pers)
        contexto={
            'formu':formu
        }   
        if formu.is_valid():
            formu.save()
            return redirect('readciudad')
           
        return render(request,'Ciudadregitro.html',contexto)
    


    return render(request,'Ciudadregitro.html',contexto)        






def eliminarciudad(request,id):
    ciu=ciudad.objects.get(id = id)
    ciu.delete()
    return redirect
    
