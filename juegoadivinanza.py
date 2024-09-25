
import random

numero_secreto = random.randint(0,100)
adivinado = False

print("bienvenido al juego de adivinar el numero secreto!")

while not adivinado:
    entrada = input("introduce un numero del 0 al 99: ") # para que el user pueda enaviar numero pero primero hay que transformar este str a numero
    numero = int(entrada) # Transformamos el str a int
    if numero == numero_secreto:
        print("Felicidades, has adivnado el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("el numero es MAYOR al ingresado")
    else: 
        print("el numero es MENOR al ingresado")