# Ejercicio 14: Escribir 10 palabras y ordenar de menor a mayor cantidad con su total de letras (palabras que contiene numero no mostrar)

def generar_frase():
    # Esta función solicita al usuario que ingrese 10 palabras
    print("Por favor, ingresa 10 palabras:")
    palabras = []
    for i in range(10):
        palabra = input(f"Palabra {i+1}: ")  # Se solicita al usuario que ingrese cada palabra
        palabras.append(palabra)  # Se agregan las palabras a la lista

    # Se filtran las palabras para incluir solo aquellas que no sean "valida" y que contengan solo letras
    palabras_filtradas = [palabra for palabra in palabras if palabra != "valida" and palabra.isalpha()]

    # Se ordenan las palabras filtradas por longitud, de menor a mayor
    palabras_ordenadas = sorted(palabras_filtradas, key=len)

    # Se crea una lista de tuplas con cada palabra y su longitud
    palabras_con_longitud = [(palabra, len(palabra)) for palabra in palabras_ordenadas]

    return palabras_con_longitud

# Se llama a la función generar_frase() para obtener la lista de palabras y su longitud
palabras_con_longitud = generar_frase()

# Se imprime la lista de palabras junto con su longitud y su número de orden
print("Palabras y su longitud:")
for i, (palabra, longitud) in enumerate(palabras_con_longitud, start=1):
    print(f"{i}. {palabra} = {longitud} letras")
