# Ejercicio 18: ingresar su nombre y su edad. Luego, sepa usted si ya es mayor o menor de edad.


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print(nombre, "ya eres mayor de edad.")
else:
    print(nombre, "aun no eres mayor de edad.")