import random

def adivinar_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 3

    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes 3 intentos para adivinar un número entre 1 y 10.")

    while intentos > 0:
        intento = int(input("Introduce tu número: "))

        if intento == numero_secreto:
            print("¡Felicidades! ¡Adivinaste el número!")
            return

        elif intento < numero_secreto:
            print("El número es más alto.")

        else:
            print("El número es más bajo.")

        intentos -= 1
        print("Te quedan {} intentos.".format(intentos))

    print("Lo siento, has agotado tus intentos. El número secreto era {}.".format(numero_secreto))

adivinar_numero()