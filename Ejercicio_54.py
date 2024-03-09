"""Ejercicio 11: Solicitar al usuario que ingrese una cadena utilizando la función prompt() 
y almacena el valor en una variable llamada cadena. Muestrar la cadena ingresada 
al usuario utilizando document.write(). Calcular y muestrar la cantidad de caracteres 
en la cadena utilizando cadena.length. Muestrar el primer carácter de la cadena 
utilizando cadena.charAt(0). Muestrar los primeros tres caracteres de la cadena 
utilizando cadena.substring(0, 3). Verifica si la subcadena 'hola' está presente 
en la cadena utilizando cadena.indexOf('hola'). Si está presente, 
muestra 'Se ingresó la subcadena hola'; de lo contrario, 
muestra 'No se ingresó la subcadena hola'. Convierte la cadena a mayúsculas 
utilizando cadena.toUpperCase() y muestrar el resultado. Conviertir la cadena 
a minúsculas utilizando cadena.toLowerCase() y muestrar el resultado"""


cadena = input('Ingrese una cadena: ')
print('La cadena ingresada es:', cadena)
print('La cantidad de caracteres son:', len(cadena))
print('El primer carácter es:', cadena[0])
print('Los primeros 3 caracteres son:', cadena[:3])
if 'hola' in cadena:
    print('Se ingresó la subcadena hola')
else:
    print('No se ingresó la subcadena hola')
print('La cadena convertida a mayúsculas es:', cadena.upper())
print('La cadena convertida a minúsculas es:', cadena.lower())
