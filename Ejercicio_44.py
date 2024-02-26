"""Ejercicio 44: Teniendo en cuenta los temarios de diccionario. Realizar un diccionario los precios 
de las Mango, Pera, Naranja y  Arandano pregunte al usuario por una fruta, kilos en numero y muestre 
el precio total de la fruta. Si la fruta no está en el diccionario 
debe mostrar un mensaje informando de ello"""


frutas = {'Mango':8.35, 'Pera':14.8, 'Naranja':25.85, 'Arandano':12.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, 'Soles')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")