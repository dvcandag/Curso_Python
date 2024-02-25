# Ejercicio 41: Teniendo en cuenta las clases de condicionales, hacer ejercicio de un programa 
# que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.



# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 45063:
    tipo = 4
elif renta < 200000:
    tipo = 3
elif renta < 54600:
    tipo = 2
elif renta < 60000:
    tipo = 1
else:
    tipo = 4
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar S/ ", renta * tipo / 100, sep='')