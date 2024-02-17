# Ejercicio 26: ingresar numeros y verificas si es un número primo

# Verificar si un número es primo
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

numero = int(input("Ingresa un número para verificar si es primo: "))
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
