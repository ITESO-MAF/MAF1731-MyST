
import random

# Persona a responder
estudiantes = ['Estudiante_1', 'Estudiante_2', 'Estudiante_3']
res1 = estudiantes[random.randint(0, 1)]

# Pregunta a responder
preguntas = ['¿Podrías explicar a detalle la función de ventana(F1,F2)?', #
             '¿Podrías explicar la celda que contiene la línea “volatilidad”? [356]', # bien
             '¿Podrías explicar a detalle la forma en la que calcularon el Draw Down?', # bien
             '¿Podrías hacer un flujo en papel o pintarron sobre el proceso completo de la función hazparo?'] #

res2 = preguntas[random.randint(0, 3)]

print(res1)
print('------')
print(res2)
