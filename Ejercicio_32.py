# Ejercicio 32: El ejercicio consta en determinar la estación dada una fecha (mes y día), 
#mostrar la estación del año correspondiente. 
# El programa debe solicitar al usuario que ingrese el número de mes (1-12) y el día (1-31), 
# y luego determinar la estación del año basándose en esa fecha.



def determinar_estacion(mes, dia):
    if mes == 1 or (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif mes == 4 or mes == 5 or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif mes == 7 or mes == 8 or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        return "Verano"
    elif mes == 10 or mes == 11 or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
        return "Otoño"
    else:
        return "Fecha inválida"

def main():
    try:
        mes = int(input("Ingresa el número de mes (1-12): "))
        dia = int(input("Ingresa el número de día (1-31): "))
        if mes < 1 or mes > 12 or dia < 1 or dia > 31:
            print("Por favor, ingresa un número de mes y día válidos.")
        else:
            estacion = determinar_estacion(mes, dia)
            print(f"La estación del año para la fecha {dia}/{mes} es: {estacion}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()
