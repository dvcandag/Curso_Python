# Ejercicio 29: Calcular la suma de los dígitos al cuadrado de un número

def suma_digitos_cuadrado(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito) ** 2
    return suma

numero = int(input("Ingresa un número: "))
print("Suma de los dígitos al cuadrado:", suma_digitos_cuadrado(numero))