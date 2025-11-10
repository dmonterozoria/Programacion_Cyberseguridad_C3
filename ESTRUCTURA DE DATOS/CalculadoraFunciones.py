#Calculadora con funciones
def mostrar_mensaje(mensaje): #funcion para imprimir mensaje
    print("***************************************")
    print(mensaje)
    print("***************************************")    

def sumar(): #funcion para sumar dos numeros
 valor1=int(input("Ingrese el primer numero a sumar: ")) #entrada del primer valor
 valor2=int(input("Ingrese el segundo numero a sumar: ")) #entrada del segundo valor  
 suma=valor1+valor2 #suma de los dos valores
 print("La suma es:",suma) #imprimir la suma

def restar(): #funcion para restar dos numeros
 valor1=int(input("Ingrese el primer numero a restar: ")) #entrada del primer valor
 valor2=int(input("Ingrese el segundo numero a restar: ")) #entrada del segundo valor  
 resta=valor1-valor2 #resta de los dos valores
 print("La resta es:",resta) #imprimir la resta

def multiplicar(): #funcion para multiplicar dos numeros
 valor1=int(input("Ingrese el primer numero a multiplicar: ")) #entrada del primer valor
 valor2=int(input("Ingrese el segundo numero a multiplicar: ")) #entrada del segundo valor  
 multiplicacion=valor1*valor2 #multiplicacion de los dos valores
 print("La multiplicacion es:",multiplicacion) #imprimir la multiplicacion

def dividir(): #funcion para dividir dos numeros
 valor1=int(input("Ingrese el primer numero a dividir: ")) #entrada del primer valor
 valor2=int(input("Ingrese el segundo numero a dividir: ")) #entrada del segundo valor  
 division=valor1/valor2 #division de los dos valores
 print("La division es:",division) #imprimir la division
 
mostrar_mensaje("Calculadora de funciones") #llamada a la funcion
sumar() #llamada a la funcion
restar() #llamada a la funcion
multiplicar() #llamada a la funcion     
dividir() #llamada a la funcion 
mostrar_mensaje("Gracias por usar la calculadora") #llamada a la funcion