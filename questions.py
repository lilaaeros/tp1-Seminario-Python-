import random
import sys 

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Qué se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Qué operador de comparación para verificar si dos valores son iguales?"
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "42", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "# Esto es un comentario",
        "'// Esto es un comentario'",
        "'/* Esto es un comentario */'",
        "'-- Esto es un comentario'"
    ),
    ("=", "==", "!", "===")
]

# Índice de la respuesta correcta para cada pregunta en el mismo orden q las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
puntos =0 

questions_to_ask = random.sample(list(zip(questions,
answers, correct_answers_index)), k=3)


# El usuario deberá contestar 3 preguntas
for question, answers_list, correct_index in questions_to_ask:

    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answers_list):
        print(f"{i + 1}. {answer}")
    
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")

# veo si la entrada es un numero
        if not user_answer.isdigit():
            print("Respuesta no valida hay q ingresar un nro")
            sys.exit(1)
        
        user_answer = int(user_answer) - 1
        
        # Verificar si la respuesta está dentro del rango permitido
        if user_answer < 0 or user_answer >= len(answers_list):
            print("Respuesta no válida")
            sys.exit(1)

        
        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            puntos += 1
            print("¡Correcto!")
            break
    else:
# Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta. 'ESTA RARA ESTA PARTE, PERO NO LA TOCO PQ ASI ESTABA EL EJ ORIGINAL'
        puntos -= 0.5
        print("Incorrecto. La respuesta correcta es:")
        print(answers_list[correct_index])
    
    # Se imprime un espacio en blanco al final de la pregunta
    print()
print ("los puntos ganados en la partida son ", puntos)