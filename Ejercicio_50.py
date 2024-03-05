"""crear un programa que repita lo que el usuario escriba hasta que decida terminar ingresando "salir"."""
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)