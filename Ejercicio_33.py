# Ejercicio 33: utilizando un diccionario llamado "gravedad_planetas", almacene la gravedad relativa de cada 
# planeta con respecto a la Tierra. Luego, define una función llamada (calcular_peso_en_planetas )que tome como 
# argumento el peso de una persona en la Tierra y devuelva un diccionario con el peso de esa persona en cada planeta,
# utilizando la gravedad correspondiente. 

# Finalmente para su calificación, muestra el peso de la persona en 7 planetas del sistema solar.







def calcular_peso_en_planetas(peso_earth):
    # Gravedad en diferentes planetas (en comparación con la Tierra)
    gravedad_planetas = {
        'Mercurio': 0.38,
        'Venus': 0.91,
        'Marte': 0.38,
        'Jupiter': 2.34,
        'Saturno': 1.06,
        'Urano': 0.92,
        'Neptuno': 1.19
    }

    # Calcular peso en cada planeta
    peso_en_planetas = {}
    for planeta, gravedad in gravedad_planetas.items():
        peso_en_planeta = peso_earth * gravedad
        peso_en_planetas[planeta] = peso_en_planeta

    return peso_en_planetas

# Peso de la persona en la Tierra
peso_earth = float(input("Ingrese su peso en la Tierra (en kilogramos): "))

# Calcular y mostrar el peso en diferentes planetas
peso_en_planetas = calcular_peso_en_planetas(peso_earth)

print("\nPeso en diferentes planetas:")
for planeta, peso in peso_en_planetas.items():
    print(f'{planeta}: {peso:.2f} kilogramos')
