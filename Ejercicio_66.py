"""
Ejercicio 66: Calculadora
Desarrollar una aplicación GUI denominada "Calculadora" que opere como una calculadora básica. La interfaz de la aplicación incluirá:

1.- Tres etiquetas identificadas como "Primer número", "Segundo número" y "Resultado".
2.- Tres campos de entrada de texto (lineEdit), donde el campo correspondiente al "Resultado" será de solo lectura.
3.- Seis botones designados para realizar operaciones aritméticas: suma (+), resta (-), multiplicación (*), división (/), 
módulo (%) y reinicio (RESET). Al presionar el botón "RESET", se eliminarán los valores ingresados en los tres campos 
de entrada de texto. Al seleccionar cualquier operador aritmético (+, -, *, / o %), solo el campo relevante se modificará 
para mostrar el resultado de la operación.

4.- nstalar la biblioteca PyQt5 usando pip en el terminal o símbolo del sistema:

pip install PyQt5

"""

#SOLUCION


import sys  # Importa el módulo sys para interactuar con el sistema operativo.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout  # Importa las clases necesarias de PyQt5 para crear la interfaz gráfica.

class CalculadoraApp(QWidget):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre.
        self.setWindowTitle('Calculadora')  # Establece el título de la ventana.
        self.setGeometry(100, 100, 200, 50)  # Establece la posición y el tamaño de la ventana.

        # Definición de etiquetas y campos de entrada.
        self.label1 = QLabel('Primer número:')
        self.label2 = QLabel('Segundo número:')
        self.label_result = QLabel('Resultado:')
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit_result = QLineEdit()
        self.lineEdit_result.setReadOnly(True)  # Hace que el campo de resultado sea de solo lectura.

        # Definición de botones.
        self.button_suma = QPushButton('+')
        self.button_resta = QPushButton('-')
        self.button_mult = QPushButton('*')
        self.button_div = QPushButton('/')
        self.button_mod = QPushButton('%')
        self.button_reset = QPushButton('RESET')

        # Configuración de la interfaz de usuario.
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()  # Crea un diseño vertical para organizar los widgets.
        layout.addWidget(self.label1)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.label2)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.label_result)
        layout.addWidget(self.lineEdit_result)
        layout.addWidget(self.button_suma)
        layout.addWidget(self.button_resta)
        layout.addWidget(self.button_mult)
        layout.addWidget(self.button_div)
        layout.addWidget(self.button_mod)
        layout.addWidget(self.button_reset)

        self.setLayout(layout)  # Establece el diseño creado como diseño principal de la ventana.

        # Conexión de los eventos de los botones con las funciones correspondientes.
        self.button_suma.clicked.connect(self.sumar)
        self.button_resta.clicked.connect(self.restar)
        self.button_mult.clicked.connect(self.multiplicar)
        self.button_div.clicked.connect(self.dividir)
        self.button_mod.clicked.connect(self.modulo)
        self.button_reset.clicked.connect(self.resetear)

    # Funciones para realizar operaciones aritméticas y mostrar el resultado.
    def sumar(self):
        num1 = float(self.lineEdit1.text())
        num2 = float(self.lineEdit2.text())
        resultado = num1 + num2
        self.lineEdit_result.setText(str(resultado))

    def restar(self):
        num1 = float(self.lineEdit1.text())
        num2 = float(self.lineEdit2.text())
        resultado = num1 - num2
        self.lineEdit_result.setText(str(resultado))

    def multiplicar(self):
        num1 = float(self.lineEdit1.text())
        num2 = float(self.lineEdit2.text())
        resultado = num1 * num2
        self.lineEdit_result.setText(str(resultado))

    def dividir(self):
        num1 = float(self.lineEdit1.text())
        num2 = float(self.lineEdit2.text())
        if num2 != 0:
            resultado = num1 / num2
            self.lineEdit_result.setText(str(resultado))
        else:
            self.lineEdit_result.setText('Error: División por cero')

    def modulo(self):
        num1 = float(self.lineEdit1.text())
        num2 = float(self.lineEdit2.text())
        if num2 != 0:
            resultado = num1 % num2
            self.lineEdit_result.setText(str(resultado))
        else:
            self.lineEdit_result.setText('Error: División por cero')

    # Función para reiniciar los campos de entrada.
    def resetear(self):
        self.lineEdit1.clear()
        self.lineEdit2.clear()
        self.lineEdit_result.clear()

# Bloque principal para ejecutar la aplicación.
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea una instancia de la aplicación PyQt.
    calc_app = CalculadoraApp()  # Crea una instancia de la clase CalculadoraApp.
    calc_app.show()  # Muestra la ventana de la calculadora.
    sys.exit(app.exec_())  # Sale de la aplicación cuando se cierra la ventana.
