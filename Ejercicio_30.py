# Ejercicio 30: Desarrolla un programa en Python que simule el lanzamiento 
# de N dados y calcule la suma de los valores obtenidos en cada lanzamiento. 


import random

def tirar_dados(num_dados, caras):
    resultados = []
    for _ in range(num_dados):
        resultado = random.randint(1, caras)
        resultados.append(resultado)
    return resultados

def main():
    print("Bienvenido al simulador de dados")
    num_dados = int(input("Ingrese el número de dados a tirar: "))
    num_caras = int(input("Ingrese la cantidad de caras en cada dado: "))

    resultados = tirar_dados(num_dados, num_caras)

    print("Resultados de los lanzamientos:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Dado {i}: {resultado}")

if __name__ == "__main__":
    main()
