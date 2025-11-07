# 1) Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):
    print(f"Factorial de {i}: {factorial(i)}")

# 2) Serie de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci: "))
for i in range(n):
    print(fibonacci(i), end=" ")
print()

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")

# 4) Decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

n = int(input("Ingrese un número decimal: "))
print(f"El número {n} en binario es: {decimal_a_binario(n)}")

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")

# 6) Suma de dígitos recursiva
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

n = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos es: {suma_digitos(n)}")

# 7) Contar bloques recursivamente
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

n = int(input("Ingrese la cantidad de bloques en el nivel inferior: "))
print(f"Total de bloques: {contar_bloques(n)}")

# 8) Contar dígito recursivamente
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito a buscar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
