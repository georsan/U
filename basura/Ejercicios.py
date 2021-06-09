#1.
#Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
#Una dirección se considerará válida si contiene el símbolo "@".

def vlidaremail(email):
    validar = '@'
    valido=False
    for palabra in email:
        if palabra==validar:
            valido=True
    if valido==True:
        print('Email es valido')
    else:
        print('Email no valido')        


#2
def sumar(numer):
    suma=0
    while numer!=0:
        digito=numer%10
        suma=suma+digito
        numer=numer//10
        print(numer)


sumar(100)