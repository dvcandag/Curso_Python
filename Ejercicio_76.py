"""
Ejercicio 76: Programa de cálculo de edades

Escribe un programa en Python que realice las siguientes tareas:

1.- Entrada de datos: El programa debe solicitar al usuario que ingrese el año actual.
2.- Registro de personas: Luego, el programa debe permitir al usuario ingresar el nombre y el año de nacimiento 
    de tres personas diferentes.
3.- Cálculo de edades: Para cada persona registrada, el programa debe calcular la edad que cumplirá durante el año actual.
4.- Presentación de resultados: Finalmente, el programa debe imprimir en pantalla el nombre de cada persona junto con la 
    edad que cumplirá durante el año en curso.

Instrucciones Adicionales:

1.- Asegúrate de que el programa maneje correctamente las entradas del usuario, proporcionando mensajes de error claros 
    en caso de entrada inválida.
2.- Fomenta la modularidad en el diseño de tu programa. Considera cómo dividir las tareas en funciones más pequeñas para facilitar 
    la comprensión y el mantenimiento del código.
3.- Piensa en casos de prueba adicionales que podrían ayudarte a verificar la corrección y robustez de tu programa. Esto podría 
    incluir situaciones como años negativos, nombres con caracteres especiales, etc.
    
"""

# SOLUCIÓN

def solicitar_año_actual():
    while True:
        try:
            # Solicita al usuario que ingrese el año actual
            año_actual = int(input("Por favor, ingresa el año actual: "))
            # Verifica si el año ingresado es válido (positivo)
            if año_actual > 0:
                return año_actual
            else:
                print("Por favor, ingresa un año válido.")
        except ValueError:
            # Maneja la excepción en caso de que el usuario ingrese un valor no numérico
            print("Por favor, ingresa un año válido.")
            
def registrar_persona(numero_persona):
    # Función para registrar los datos de una persona
    nombre = input(f"Ingrese el nombre de la persona {numero_persona}: ")
    while True:
        try:
            # Solicita al usuario que ingrese el año de nacimiento de la persona
            año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
            año_actual = solicitar_año_actual()
            # Verifica si el año de nacimiento es válido (menor o igual al año actual)
            if año_nacimiento > año_actual:
                print("El año de nacimiento no puede ser mayor que el año actual.")
            else:
                return nombre, año_nacimiento, año_actual
        except ValueError:
            # Maneja la excepción en caso de que el usuario ingrese un valor no numérico
            print("Por favor, ingresa un año válido.")
            
def calcular_edad(año_nacimiento, año_actual):
    # Calcula la edad restando el año de nacimiento del año actual
    return año_actual - año_nacimiento

def presentar_resultados(registros):
    # Función para presentar los resultados
    print("\nResultados:")
    for nombre, año_nacimiento, año_actual, edad in registros:
        # Imprime el nombre de la persona y la edad que cumplirá durante el año actual
        print(f"{nombre} cumplirá {edad} años durante el año {año_actual}.")

def main():
    # Función principal
    año_actual = solicitar_año_actual()
    registros = []
    for i in range(1, 4):
        print(f"\nPersona {i}:")
        nombre, año_nacimiento, año_actual = registrar_persona(i)
        edad = calcular_edad(año_nacimiento, año_actual)
        # Almacena los datos de la persona y su edad en una lista de registros
        registros.append((nombre, año_nacimiento, año_actual, edad))
    presentar_resultados(registros)
    
if __name__ == "__main__":
    main()
    