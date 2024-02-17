# Ejercicio 25: Emplenado la función ord() para obtener el valor ASCII de un carácter y chr() para convertir un valor ASCII imprimir el abecedario en mayusculas.


print("Abecedario en mayúsculas:")
for letra in range(ord('A'), ord('Z')+1): # "A=mayuscula, a=minuscula"
    print(chr(letra), end=" ")
print()