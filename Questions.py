import random
# Preguntas para el juego
questions = [ "¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
Puntuacion=0
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)
preguntas_a_preguntar=random.sample(questions_to_ask,3)
# El usuario deberá contestar 3 preguntas
for Pregunta,respuestas,RespuestaCorrecta in preguntas_a_preguntar:
    print(Pregunta)
    for i, answer in enumerate(respuestas):
        print(f"{i + 1}. {answer}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = int(input("Respuesta: ")) - 1
        if user_answer < 0 or  user_answer >= 4:
            print("Respuesta no Valida")
            exit(1)
        #   Se verifica si la respuesta es correcta
        if user_answer == RespuestaCorrecta:
            Puntuacion+=1
            print("¡Correcto!")
            break
        else:
            Puntuacion-=0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(respuestas[RespuestaCorrecta])
# Se imprime un blanco al final de la pregunta
print(Puntuacion)
print()

