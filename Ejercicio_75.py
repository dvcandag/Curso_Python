"""
Ejercicio 75: conversor de números
Construir un pequeño programa que convierta números binarios en enteros.

"""

# SOLUCIÓN

def binario_a_entero(numero_binario):
    #Convierte un número binario en un entero.
   
    entero = 0
    for digito in numero_binario:
        entero = entero * 2 + int(digito)
    return entero

def programa_principal():
    #Función principal del programa.
    
    numero_binario = input("Ingrese un número binario: ")
    
    #Validación de la entrada para asegurarse de que es un número binario
    if not all(digito in '01' for digito in numero_binario) or len(numero_binario) == 0:
        print("Entrada inválida. Por favor, ingrese solo secuencias válidas de 0s y 1s.")
        return
    
    # Convertir el número binario en un entero
    entero = binario_a_entero(numero_binario)
    
    print("El número binario {} equivale al entero {}.".format(numero_binario, entero))

# Llamar a la función principal
if __name__ == "__main__":
    programa_principal()

