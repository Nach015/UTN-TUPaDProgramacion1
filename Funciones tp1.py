#Punto 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#Punto 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#Punto 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_ingresado = input("Ingresa tu nombre: ")
apellido_ingresado = input("Ingresa tu apellido: ")
edad_ingresada = input("Ingresa tu edad: ")
residencia_ingresada = input("Ingresa tu residencia: ")

informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)

#Punto 4
PI = 3.14159

def calcular_area_circulo(radio):
    return PI * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"\nResultados para el radio {radio}:")
print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")

#Punto 5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos_ingresados = float(input("Ingresa una cantidad de segundos: "))
horas = segundos_a_horas(segundos_ingresados)
print(f"{segundos_ingresados} segundos equivalen a {horas} horas.")

#Punto 6

def tabla_multiplicar(numero):
    print(f"\n--- Tabla del {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero_tabla = int(input("Ingresa el número para ver su tabla de multiplicar (1-10): "))
tabla_multiplicar(numero_tabla)

#Punto 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (División por cero)"
        
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingresa el primer número (a): "))
num2 = float(input("Ingresa el segundo número (b): "))

resultados = operaciones_basicas(num1, num2)

print("\n--- Resultados de las Operaciones ---")
print(f"Suma (a + b): {resultados[0]}")
print(f"Resta (a - b): {resultados[1]}")
print(f"Multiplicación (a * b): {resultados[2]}")
print(f"División (a / b): {resultados[3]}")

#Punto 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso_kg = float(input("Ingresa tu peso en kilogramos (ej: 70.5): "))
altura_mts = float(input("Ingresa tu altura en metros (ej: 1.75): "))

imc = calcular_imc(peso_kg, altura_mts)
print(f"\nTu Índice de Masa Corporal (IMC) es: {imc}")

#Punto 9 

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

print(f"\n{temp_celsius}°C equivalen a {temp_fahrenheit:}°F.")

#Punto 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num_a = float(input("Ingresa el primer número: "))
num_b = float(input("Ingresa el segundo número: "))
num_c = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(num_a, num_b, num_c)

print(f"\nEl promedio de {num_a}, {num_b}, y {num_c} es: {promedio}")