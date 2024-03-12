"""Ejercicio 55: 

Desarrolla una clase "Hipervinculo" en Python que represente un hipervínculo HTML 
con dos atributos: "direccion" y "titulo". La clase debe incluir un método llamado 
"retornar_hipervinculo" que devuelve el hipervínculo en formato HTML válido. Además, 
crea una lista llamada "vector" que contendrá tres objetos de la clase Hipervinculo. 
Asegúrate de seguir el estilo de codificación de Python, proporcionar comentarios 
explicativos. Tu solución debe entregarse en un archivo .py"""

# Definición de la clase Hipervinculo
class Hipervinculo:
    # Método constructor que inicializa los atributos direccion y titulo
    def __init__(self, direccion, titulo):
        self.direccion = direccion  # Asigna la dirección del hipervínculo
        self.titulo = titulo  # Asigna el título del hipervínculo
    
    # Método para retornar el hipervínculo en formato HTML válido
    def retornar_hipervinculo(self):
        # Crea la cadena HTML con la dirección y el título del hipervínculo
        cadena = f'<a href="{self.direccion}">{self.titulo}</a>'
        return cadena  # Retorna la cadena HTML del hipervínculo

# Creación de una lista llamada vector que contendrá tres objetos de la clase Hipervinculo
vector = []
vector.append(Hipervinculo('https://www.google.com', 'google'))  # Añade un hipervínculo a la lista
vector.append(Hipervinculo('https://www.msn.com', 'msn'))  # Añade otro hipervínculo a la lista
vector.append(Hipervinculo('https://www.facebook.com', 'yahoo'))  # Añade un tercer hipervínculo a la lista

# Itera sobre los objetos en la lista vector e imprime el hipervínculo HTML de cada objeto
for hipervinculo in vector:
    print(hipervinculo.retornar_hipervinculo())
