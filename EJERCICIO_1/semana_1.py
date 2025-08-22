#Ejercicio1
#Crear unprograma que imprima por pantalla el mensaje: "Hola Mundo!"
print ("Hola Mundo!")

#Ejercicio2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo, si el usuario ingresa "Marcos", elprograma debe imprimir por pantalla "Hola Marcos!"
print ("Bienvenido!")
nombre=input("Cómo te llamas?")
print(f"Hola, {nombre}") 

#Ejercicio3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
print("Bienvenido/a!")
nombre_apellido=input("Por favor, completa los siguientes datos. Nombre y apellido: ")
edad=input("Edad: ")
lugar=input("Lugar de residencia:")
print(f"Soy {nombre_apellido}, tengo {edad} años y vivo en {lugar}")

#Ejercicio4
#Crear un programa quepida al usuario el radio de un circulo e imprima por pantalla su area y su perimetro
print("Bienvenido!")
radio=float(input("Por favor ingresa el radio de un círculo:"))
area=(3.14159*radio**2)
perimetro=(2 * 3.14159 * radio)
print (f"Su área es  {area}  y su perímetro es  {perimetro}")

#Ejercicio5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
print ("Bienvenido!")
segundos=float(input("Dime una cantidad de segundos y te diré su equivalente en horas:"))
hora=(segundos//3600)
print(f"Su equivalente es: {hora}")

#Ejercicio6
#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("Bienvenido!")
numero=float(input("Por favor, ingresa un número y te haré la trabla de multiplicar de ese número:"))
#Busqué en los apuntes de actividades, en el microteaching y no encuentro cómo hacer el rango de 1 a 10. Sé que si lo pongo en chatgpt me va a dar la respuesta pero quiero la explicación. 

#Ejercicio7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("Bienvenido!")
num1=int(input("Por favor, ingresa un número entero que no sea 0:"))
num2=int(input("Ahora ingresa otro número que no sea 0 y te haré las operaciones matemáticas entre ambos:"))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Si lo sumo el resultado es: {suma}, si resto el resultado es {resta}, si divido: {division} y si multiplico: {multiplicacion}")

#Ejercicio8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
print("Bienvenido! Veremos cuál es tu Índice de Masa Corporal")
altura=float(input("Por favor, ingresa tu altura en metros:"))
peso=float(input("Ahora ingresa tu peso en kilos:"))
imc=(peso/(altura**2))
print("Tu IMC es:" , (imc))

#Ejercicio9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print("Bienvenido!")
gradosc=float(input("Cuál es tu temperatura en grados Celcius?:"))
gradof=(9/5)*(gradosc)+32
print(f"Esa temperatura en grados Fahrenheites: {gradof}")

#Ejercicio10
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("Bienvenido!")
num1=float(input("Por favor, ingresa un número:"))
num2=float(input("Ahora, ingresa un segundo número:"))
num3=float(input("Finalmente, ingresa un tercer número:"))
promedio=(num1+num2+num3)/3
print("El promedio de estos tres números es igual a: ", promedio)