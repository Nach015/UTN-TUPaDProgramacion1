

# 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3)
frutas = list(precios_frutas.keys())
print(frutas)

# 4)
telefonos = {}
for i in range(5):
    nombre = input("Nombre: ")
    numero = input("Número: ")
    telefonos[nombre] = numero

buscar = input("Ingresá un nombre para buscar: ")
if buscar in telefonos:
    print("Número:", telefonos[buscar])
else:
    print("No se encontró ese contacto.")

# 5)
frase = input("Ingresá una frase: ")
palabras = frase.split()
unicas = set(palabras)
print("Palabras únicas:", unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Cantidad por palabra:", conteo)

# 6)
alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(nombre, "promedio:", promedio)

# 7)
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}
print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# 8)
stock = {'Pan': 10, 'Leche': 5, 'Huevos': 12}
producto = input("Producto a consultar: ")
if producto in stock:
    print("Stock actual:", stock[producto])
    agregar = int(input("Unidades a agregar: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("No existe. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock
print(stock)

# 9)
agenda = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '15:00'): 'Clase',
    ('Viernes', '19:00'): 'Cine'
}
dia = input("Día: ")
hora = input("Hora: ")
if (dia, hora) in agenda:
    print("Evento:", agenda[(dia, hora)])
else:
    print("No hay actividad en ese horario.")

# 10)
paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Perú': 'Lima'}
capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais
print(capitales)
