# Calcular r el factorial de un número 5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")