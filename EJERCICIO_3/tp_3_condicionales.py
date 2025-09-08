#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad=input("Bienvenido! Para continuar, por favor, ingresa tu edad: ")
if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota=input ("Hola! Por favor ingresa tu nota:")
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
num= int(input("Bienvenido! Voy a necesitar que ingreses un número entero:"))
if num % 2 == 0:
    print ("Ha ingresado un numero par")
else:
    print ("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad=int(input("Hola! Podrías decirme tu edad?"))
if edad < 12: 
    print("Eres un/a niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un/a adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un/ adulto/a joven")
elif edad >= 30:
    ("Eres un Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso ontrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
clave=input("Bienvenido! A continuación, ingresa tu contraseña:")
if len(clave) >= 8 and len(clave) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html. La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
import random
from statistics import mean, mode, median
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda= mode(numeros_aleatorios) 
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")    
elif media == mediana == moda:
    print("Sin sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó  el usuario e imprimirlo por pantalla.
nombre= input("Hola! Por favor, ingresa ntu nombre:")
vocales=(a,A,e,E,i,I,o,O,u,U)
if nombre[-1] in vocales:
    string=nombre + "!"
else:
    string=nombre
print(string)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre=input("Bienvenido/a! Cuál es tu nombre?")
formato=input("Por favor, ingresa el numero para elegir un formato: 1 para mayúsculas, 2 para minúsculas, 3 para primera letra en mayúscula")
if formato == 1:
    nombre_final = nombre.upper()
elif formato == 2:
    nombre_final= nombre.lower()
elif formato == 3:
    nombre_final= nombre.title()
else:
    nombre_final= "No se puede establecer un formato"
print(nombre_final)

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magni=input("Hola! Hemos sentido ese terremoto! Podrias indicarnos la magnitud para calcular el impacto?")
if magni < 3:
    print("Muy leve")
elif 3 <= magni < 4:
    print("Leve")
elif 4 <= magni < 5:
    print("Moderado")
elif 5 <= magni < 6:
    print("Fuerte")
elif 6 <= magni < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemis=input("Hola! Podrías decirme en qué hemisferio estás si 'N' o 'S'?")
mes=int(input("y ahora, dime, qué mes del año es?"))
dia=int(input("y qué día?"))
if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
else:
    estacion_norte = "Fecha Inválida"

estacion_final = ""

if hemis == 'N':
    estacion_final = estacion_norte
elif hemis == 'S':
    if estacion_norte == "Invierno":
        estacion_final = "Verano"
    elif estacion_norte == "Primavera":
        estacion_final = "Otoño"
    elif estacion_norte == "Verano":
        estacion_final = "Invierno"
    elif estacion_norte == "Otoño":
        estacion_final = "Primavera"
    else:
        estacion_final = estacion_norte
else:
    estacion_final = "Hemisferio no reconocido"

if estacion_final in ["Hemisferio no reconocido", "Fecha Inválida"]:
    print(estacion_final)
else:
    print(f"\nEstás en **{estacion_final}**.")

