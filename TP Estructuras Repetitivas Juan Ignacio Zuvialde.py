#Punto 1
for numero in range(101):
    print(numero)
print(" ")

#Punto 2
numero = input("Por favor, ingresa un número entero: ")

cantidad_de_digitos = len(numero)

print(f"El número ingresado tiene {cantidad_de_digitos} dígitos.")

#Punto 3

numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))

if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1

suma_total = 0

for numero in range(numero_1 + 1, numero_2):
    suma_total += numero

print(f"La suma de los números entre {numero_1} y {numero_2} es: {suma_total}")

#Punto 4
suma_total = 0

print("Ingresa números enteros para sumarlos.")
print("Escribe 0 para terminar y ver el total.")

while True:
    numero = int(input("Ingresa un número: "))
    
    if numero == 0:
        break
    suma_total += numero

print(f"La suma total es: {suma_total}")

#Punto 5
import random

numero_azar = random.randint(0, 9)

intentos = 0

print("¡Bienvenido! Adivina un número entre 0 y 9. ")

while True:
    
    numero_del_usuario = int(input("Ingresa tu número: "))
    
    intentos += 1
    
    if numero_del_usuario == numero_azar:
        print(f"¡Excelente! Adivinaste el número {numero_azar} en {intentos} intento(s).")
        break  
    else:
        print("El número es incorrecto ¡Proba de nuevo! ")

#Punto 6

numero = 100

while numero >= 0:
    print(numero)
    numero -= 2

#Punto 7
limite = int(input("Ingresa un número entero positivo: "))

if limite < 0:
    print("Por favor, ingresa un número positivo.")
else:
    suma = 0

    for numero in range(limite + 1):
        suma += numero
    print(f"La suma de todos los números desde 0 hasta {limite} es: {suma}")

#Punto 8

cant_nums=100

impares=0
pares=0
negativos=0
positivos=0

print(f"Ingresa {cant_nums} numeros por favor")

for i in range(cant_nums):
    num=int(input(f"numero {i +1}: "))
    if num>0:
        positivos+=1
    elif num<0:
        negativos+=1
    
    if num % 2==0:
        pares+=1
    else:
        impares+=1
print("RESULTADOS!! ")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#Punto 9

cant_num=100

suma=0 

print(f"Ingrese {cant_num} numeros por favor: ")

for i in range(cant_num):
    num=float(input(f"Ingrese el numero {i+1} por favor:"))
    suma+=num


media=suma/cant_num
print(f"La media es: {media}")

#Punto 10
numero = int(input("Ingresa un número para invertir: "))
numero_invertido = 0
while numero > 0:
    ultimo_digito = numero % 10
    numero_invertido = numero_invertido * 10 + ultimo_digito
    numero = numero // 10
print("El número invertido es:", numero_invertido)