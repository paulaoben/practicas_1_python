"""1) Escribí un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre. A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.

Ejemplo de ejecución:

Tu nombre: Patricia
Ahora estás en la matrix, Patricia"""

nombre = input("Ingrese su nombre: ")

print(f"Ahora estás en la matrix, {nombre}")

"""Solución dada:

nombre=input("Tu nombre:")
print("Ahora estás en la matrix,", nombre)"""


"""2) Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.
 
Ejemplo de ejecución:

Primer número: 14.2
Segundo número: 19
El resultado de la suma es 33.2"""

decim = float(input("Ingrese un número con decimales: "))
ent = int(input("Ingrese un número entero: "))
resultado = decim + ent

print(f"El resultado de la suma es: {resultado}")

"""Solución dada:

a=float(input("Primer número:"))
b=int(input("Segundo número:"))
c=a+b
print("El resultado de la suma es", c)"""


"""3) Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
 
Ejemplo de ejecución:

Ingresá un número: 1
Ingresá otro número: 2
Suman: 3
Ingresá un nuevo número: 3
Multiplicación de la suma por el último número: 9"""

primer = float(input("Ingrese un número: "))
seg = float(input("Ingrese otro número: "))
suma = primer + seg
print(f"El resultado de la suma es: {suma}")
tercer = float(input("Ingrese un tercer número: "))

respuesta = suma * tercer

print(f"La multiplicación de la suma por el tercer número es: {respuesta}")

"""Solución dada:

n1=int(input("Ingresá un número:"))
n2=int(input("Ingresá otro número:"))
suma=n1+n2
print("Suman:", suma)
n3=int(input("Ingresá un nuevo número:"))
print("Multiplicación de la suma por el último número:",suma*n3)"""

"""4) Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.
 
Ejemplo de ejecución:

Kilómetros recorridos: 260
Litros de combustible gastados: 12.5
El consumo por kilómetro es de 20.8"""

km = float(input("Indique la cantidad de kilómetros recorridos en motocicleta: "))
lts = float(input("Indique la cantidad de litros que consumió en ese recorrido: "))

print(f"El consumo de combustible por kilómetro es: {km/lts}")

"""Solución dada:

kilometros=float(input("Kilómetros recorridos:"))
litros=float(input("Litros de combustible gastados:"))
print("El consumo por kilómetro es de", kilometros/litros)"""


"""5) Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
 
Ejemplo de ejecución:

Ingresá una temperatura expresada en Farenheit: 75
23.88888888888889"""

fahrenheit = float(input("Ingrese una temperatura en escala Fahrenheit: "))
celcius = (fahrenheit - 32) * (5/9)

print(f"El resultado de su conversión de grados Fahrenheit a Celcius es: {celcius}")

"""Solución dada: 

Fahrenheit=float(input("Ingresá una temperatura expresada en Fahrenheit:"))
print((5/9) * (Fahrenheit-32))"""


"""6) Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
 
Ejemplo de ejecución:

Primer número: 8.5
Segundo número: 10
Tercer número: 5.5
El promedio de los tres es 8.0"""

uno = float(input("Ingrese un primer número: "))
dos = float(input("Ingrese un segundo número: "))
tres = float(input("Ingrese un tercer número: "))

print(f"El promedio de los tres números es {(uno + dos + tres)/3}")

"""Solución dada:

n1=float(input("Primer número:"))
n2=float(input("Segundo número:"))
n3=float(input("Tercer número:"))
print("El promedio de los tres es", (n1+n2+n3)/3)"""


"""7) Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.
 
Ejemplo de ejecución:

Ingresá un número: 260
Descontando el 15% queda: 221.0"""

#Explicación de la lógica aplicada a este ejercicio: Si un pantalón cuesta $799 y tiene un descuento del 15%, debemos pensar en el restante del 100%: 100-15=85. Para seguir indagando en cómo sacar porcentaje, después que sabemos cuál es el restante, debemos multiplicar el precio total por el restante del total: 799 x 0.85= 679.15 pesos. Ejemplo propio con el 75%:
#num2 = float(input("Ingrese un número: ")) * (0.25)
#print(f"Aplicado el %75 da como resultado: {num2}")

num1 = float(input("Ingrese un número: ")) * (0.85)
print(f"Descontando el 15% queda: {num1}")

"""Solución dada:

numero=int(input("Ingresá un número:"))
print("Descontando el 15% queda:", numero-(numero*15)/100)"""


"""8) Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla.
 
Ejemplo de ejecución:

Primera palabra: derribando
Segunda palabra: muros
derribando muros"""

word1 = (input("Ingrese una palabra: ")).title()
word2 = (input("Ingrese otra palabra: ")).lower()
phrase = word1 + " " + word2
print(f"{phrase}")

"""Solución dada:

palabra1=input("Primera palabra:")
palabra2=input("Segunda palabra:")
frase=palabra1+" "+palabra2
print(frase)"""


"""9) Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.
 
Ejemplo de ejecución:

Ingresá un texto: En un lugar de La Mancha, de cuyo nombre no quiero acordarme…
El carácter en primer lugar es: E
Ingresá un número positivo menor a 63
7
El carácter en esa posición es: u"""

txt = input("Ingrese un texto: ").title()
print(f"El caracter en primer lugar es: {txt[0]}")
indice = int(input(f"Ingrese un número positivo entero menor a {len(txt)}: "))
print(f"El caracter en esa posición es: {txt[indice]}")

"""Solución dada:
cadena=input("Ingresá un texto:")
print("El carácter en primer lugar es:", cadena[0])
print("Ingresá un número positivo menor a", len(cadena))
indice=int(input())
print("El carácter en esa posición es:", cadena[indice])
"""


"""10) Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.
 
Ejemplo de ejecución:

Shows vistos en el último año: 3
False"""

nShows = int(input("Ingrese la cantidad de shows que vio este año: "))
if nShows > 3:
    print("True")
else:
    print("False")

"""shows=int(input("Shows vistos en el último año:"))
print(shows>3)"""
