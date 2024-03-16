"""
    Ejercicio 59:
    Desarrollar un programa que reciba un diccionario con las asignaturas y las notas de un alumno
    y devuelve otro diccionario con las asignaturas en mayúsculas y las calificaciones
    correspondientes a las notas aprobadas.

    Argumentos:
    notas: Un diccionario que contiene las asignaturas como claves y las notas como valores.

    Retorna:
    Un nuevo diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas iguales o mayores a 12.
    """

#SOLUCION

def notas_aprobadas(notas):
    notas_aprobadas = {}
    for asignatura, nota in notas.items():
        if nota >= 12:  # Consideramos aprobadas las notas iguales o mayores a 12
            notas_aprobadas[asignatura.upper()] = nota
    return notas_aprobadas

# Ejecución de desarrollo:
notas_alumno = {
    'Matemáticas': 7,
    'Ciencias': 10,
    'Historia': 14,
    'Literatura': 13,
    'Inglés': 8
}

notas_aprobadas = notas_aprobadas(notas_alumno)
print(notas_aprobadas)
