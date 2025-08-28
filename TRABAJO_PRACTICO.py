#Actividad 1
print("Hola Mundo")

#Actividad 2
nombre=("Ignacio")
print("Hola ", nombre,"!")

#Actividad 3
nombre=(input("Como es tu nombre? "))
apellido=input("Como es tu apellido? ")
edad=int(input("Que edad tienes? "))
residencia=input("Cual es tu lugar de resilencia? ")

print ("Soy ", nombre, apellido, " tengo ", edad," años y soy de ", residencia)

#Actividad 4
radio=float(input("Ingrese el valor del radio: "))
area=(3.14*radio**2)
perimetro=(2*3.14*radio)

print("el area es: ", area, " y su perimetrto es: ",perimetro)

#Actividad 5

segundos=int(input("Ingrese la cantidad de segundos "))
horas=segundos/3600

print(segundos,"segundos equivalen a ", horas,"horas")

#Actividad 6
num=int(input("Ingrese el numero del que desee saber su tabla "))
print(num, "x 1 =", num*1)
print(num, "x 2 =", num*2)
print(num, "x 3 =", num*3)
print(num, "x 4 =", num*4)
print(num, "x 5 =", num*5)
print(num, "x 6 =", num*6)
print(num, "x 7 =", num*7)
print(num, "x 8 =", num*8)
print(num, "x 9 =", num*9)
print(num, "x 10 =", num*10)

#Actividad 7
num1=int(input("Ingrese el valor del primer numero (no puede ser 0)"))
num2=int(input("ingresa el valor del segundo numero (no puede ser 0)"))

print(num1, "+", num2, "=", num1+num2)
print(num1, "-", num2, "=", num1-num2)
print(num1, "x", num2, "=", num1*num2)
print(num1, "/", num2, "=", num1/num2)

#Actividad 8
altura=float(input("Ingrese cual es su altura "))
peso=int(input("Ingrese cual es su peso "))
imc=peso/altura**2

print("El indice de peso corporal es ", imc)

#Actividad 9 
celsius=int(input("Ingrese la temperatura en grados Celsius "))
fahrenheit= celsius * 9.5 +32
print(celsius, " grados celsius equivalen a ",fahrenheit, " grados fahrenheit" )

#Actividad 10
num1=float(input("Ingrese el valor del primer numero: "))
num2=float(input("Ingrese el valor del segundo numero: "))
num3=float(input("Ingrese el valor del tercer numero: "))
suma=num1+num2+num3 
promedio=suma/3

print("El promedio de los 3 numeros es: ", promedio)