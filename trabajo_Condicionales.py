#Punto 1
edad=int(input("Cual es tu edad?"))
if edad >= 18:
    print("Sos mayor de edad")
print("Fin de verificacion de edad")

#Punto 2
nota=int(input("Ingrese su nota"))

if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")
print("Fin de verificacion de notas")

#Punto 3
num=int(input("Ingrese un numero para saber si es par o impar"))

if num % 2==0:
    input("Ha ingreado un numero par")
else:
    input("Por favor ingrese un numero par")
print("Fin de verificacion")

#Punto 4
edad=int(input("Ingrese su edad "))

if edad < 12:
    print("Eres un niño")
elif edad>=12 and edad < 18:
    print("Eres un adolescente")
elif edad >=18 and edad < 30:
    print("Eres un adulto/a joven")
else:
    print("Eres un adulto")
print("Fin de verificacion")    

#Punto 5
contra=input("Ingrese una contraseña que tenga entre 8 y 14 caracteres ")

if len(contra)>= 8 and len(contra)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("Fin de verificacion")

#Punto 6
from statistics import mean, median, mode
import random

numeros_aleatorios = [random.randint(1, 50) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")
if moda is None:
    print("No se puede determinar el sesgo porque no hay una moda clara.")
elif media > mediana > moda:
    print("Sesgo positivo ")
elif media < mediana < moda:
    print("Sesgo negativo ")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No hay un sesgo claro.")

#Punto 7
frase=input("Ingrese una palabra o frase")

if frase[-1] in "aeiou":
    print(frase,"!")
else:
    print(frase)
print("fin de verificacion")

#Punto 8
nombre=input("Ingrese su nombre")
print("Eliga una opcion de como desea que se imprima su nombre")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula")

opcion=int(input("Ingrese una opcion (1,2 o 3)"))

if opcion == 1:
    print("Resultado:", nombre.upper())
elif opcion == 2:
    print("Resultado:", nombre.lower())
elif opcion == 3:
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor ingresa 1, 2 o 3.")
print("Fin de verificacion")

#Punto 9

magnitud=float(input("Ingrese la magnitud del terremoto"))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >=6 and magnitud <7:
    print("Muy fuerte (puede causar daños en estructuras débiles)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
print("Fin de verificacion")

#Punto 10
hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")
hemisferio = hemisferio.lower()
mes = int(input("Por favor, ingrese el mes del año: "))
dia = int(input("Por favor, ingrese el día del mes: "))

if hemisferio == "s":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Verano")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Otoño")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Invierno")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Primavera")
elif hemisferio == "n":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Invierno")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Primavera")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Verano")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Otoño")
print("Fin de verificacion")
