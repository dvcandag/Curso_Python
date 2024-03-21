"""
Ejercicio 64: Operaciones matemáticas
Vitto tiene N dólares. Luis tiene la mitad de la cantidad de dinero que Vitto posee, mientras que 
José tiene la mitad de la suma de lo que Vitto y Luis tienen juntos. Se desea calcular el promedio
de la cantidad de dinero que poseen entre los tres y redondearlo al número entero más cercano.


Proporcionar comentarios explicativos. Tu solución debe entregarse en un archivo .py 
ejecutandose satisfactoriamente en el terminal de su entorno de desarrollo.
"""


# SOLUSION

# Definición de la cantidad de dinero que tiene Vitto
vitto = 47  # Cantidad de dinero que tiene Vitto (cambia este valor según sea necesario)

# Calculando la cantidad de dinero que tiene Luis, que es la mitad de lo que tiene Vitto
luis = vitto / 2  # Luis tiene la mitad de lo que tiene Vitto

# Calculando la cantidad de dinero que tiene José, que es la mitad de la suma de lo que tienen Vitto y Luis juntos
jose = (vitto + luis) / 2  # José tiene la mitad de la suma de lo que tienen Vitto y Luis juntos

# Calculando el promedio de la cantidad de dinero que poseen entre Vitto, Luis y José
promedio = round((vitto + luis + jose) / 3)  # Calculando el promedio y redondeándolo al número entero más cercano

# Mostrando el promedio en la consola
print(f"El promedio de la cantidad de dinero que poseen entre Vitto, Luis y José es de: {promedio}")

