"""
Ejercicio 68: Sistema Decimal a Romanos

Crear una clase en Python que convierta un número entero en su equivalente en números romanos. 

Añadir comentarios para explicar el funcionamiento del código. 
El código de ejemplo proporcionado debe estar encapsulado en un archivo .py que sea ejecutable.

"""
# SOLUCION

class DecimalARomano:
    def __init__(self):
        # Diccionario que mapea valores decimales a símbolos romanos
        self.romanos = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

    def convertir_a_romano(self, num):
        """
        Convierte un número entero a su equivalente en números romanos.
        
        :param num: El número entero que se va a convertir.
        :return: La representación en números romanos del número dado.
        """
        resultado = ''  # Inicializamos el resultado como una cadena vacía
        
        # Iteramos sobre los valores romanos en orden descendente
        for valor in sorted(self.romanos.keys(), reverse=True):
            # Mientras el número sea mayor o igual al valor romano actual
            while num >= valor:
                # Concatenamos el símbolo romano correspondiente al resultado
                resultado += self.romanos[valor]
                # Restamos el valor romano del número original
                num -= valor
        
        return resultado  # Devolvemos el resultado de la conversión

# Ejemplo de uso
if __name__ == "__main__":
    conversor = DecimalARomano()  # Creamos una instancia de la clase DecimalARomano
    numero = int(input("Ingrese un número entero positivo: "))  # Solicitamos al usuario que ingrese un número
    if numero <= 0:
        print("El número debe ser positivo.")
    else:
        romano = conversor.convertir_a_romano(numero)  # Convertimos el número ingresado a su forma romana
        print(f"El número romano equivalente es: {romano}")  # Imprimimos el resultado
