# Ejercicio 34: Corregir el siguiente desarrollo e imprimir en su pantalla

'''
for planeta = diametro in diametro_planetas.items():
   diametro_planetas = {
    Mercurio: 4879 = diametro
    Venus: 12104 = diametro
    Tierra: 12756 = diametro
    Marte": 6792 = diametro
    Júpiter: 142984 = diametro
    Saturno: 120536 = diametro
    Urano: 51118 = diametro
    Neptuno: 49528 = diametro
}
for planeta, diametro.items():
    print(El diámetro de {planeta} es de {diametro} kilómetros.")
'''


# Código corregido
diametro_planetas = {
    "Mercurio": 4879,
    "Venus": 12104,
    "Tierra": 12756,
    "Marte": 6792,
    "Júpiter": 142984,
    "Saturno": 120536,
    "Urano": 51118,
    "Neptuno": 49528
}

# Diámetro de cada planeta
for planeta, diametro in diametro_planetas.items():
    print(f"El diámetro de {planeta} es de {diametro} kilómetros.")