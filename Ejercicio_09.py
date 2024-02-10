# Ejercicio 9: AMúltiplos Comunes


def multiplos_comunes(num1, num2):
    multiplos = []  # Lista para almacenar los múltiplos comunes
    maximo = max(num1, num2)  # Encontrar el máximo entre num1 y num2
    for i in range(1, maximo + 1):  # Iterar desde 1 hasta el máximo (inclusive)
        if i % num1 == 0 and i % num2 == 0:  # Verificar si i es múltiplo de ambos num1 y num2
            multiplos.append(i)  # Si es así, agregar i a la lista de múltiplos comunes
    return multiplos  # Devolver la lista de múltiplos comunes

# Ejemplo de uso:
num1 = 7  # Definir el primer número
num2 = 1  # Definir el segundo número
print("Múltiplos comunes de", num1, "y", num2, ":", multiplos_comunes(num1, num2))  # Imprimir los múltiplos comunes
