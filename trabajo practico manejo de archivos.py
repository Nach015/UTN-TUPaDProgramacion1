#Punto1
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,300.0,15\n")
    archivo.write("Goma,80.0,50\n")


#Punto2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()              
        partes = linea.split(",")           

        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]

        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Punto3
print("\nAgregar un nuevo producto:")
nuevo_nombre = input("Nombre: ")
nuevo_precio = input("Precio: ")
nueva_cantidad = input("Cantidad: ")


with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

#Punto4
productos = []   
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()          
        partes = linea.split(",")      

        
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),     
            "cantidad": int(partes[2])      
        }

        
        productos.append(producto)



#Punto5
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        producto = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        productos.append(producto)


nombre_buscado = input("Ingrese el nombre del producto a buscar: ")


encontrado = False  

for p in productos:
    if p["nombre"] == nombre_buscado: 
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break  

if not encontrado:
    print("\n No se encontró ningún producto con ese nombre.")
#Punto6
with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("\n Archivo 'productos.txt' actualizado correctamente.")