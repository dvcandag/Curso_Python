# Ejercicio 31: El ejercicio consta en determinar la estación del año según el número de mes ingresado por el usuario. 
# El programa debe solicitar al usuario que ingrese un número entero entre 1 y 12 que represente el mes.

def determinar_estacion(mes):
    if mes in (1, 2, 12):
        return "Invierno"
    elif mes in (3, 4, 5):
        return "Primavera"
    elif mes in (6, 7, 8):
        return "Verano"
    elif mes in (9, 10, 11):
        return "Otoño"
    else:
        return "Mes inválido"

def main():
    try:
        mes = int(input("Ingresa el número de mes (1-12): "))
        if mes < 1 or mes > 12:
            print("Por favor, ingresa un número de mes válido (1-12).")
        else:
            estacion = determinar_estacion(mes)
            print(f"La estación del año para el mes {mes} es: {estacion}")
    except ValueError:
        print("Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main()
