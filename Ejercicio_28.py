# Ejercicio 28: ingresar numero y generar números primos en un rango no mayor a número ingresado

def es_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generar números primos en un rango 
def generar_primos(rango):
    primos = []
    for num in range(2, rango + 1):
        if es_primo(num):
            primos.append(num)
    return primos

rango = int(input("Ingresa un rango para generar números primos: "))
print("Números primos en el rango:", generar_primos(rango))
