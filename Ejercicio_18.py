# Ejercicio 18: Ingresar un número y mostrar los siguientes múltiplos por 5


numero = int(input("Ingrese un número: "))
multiplos = [numero * i for i in range(1, 6)]
print("Los múltiplos de", numero, "por 5 son:", multiplos)