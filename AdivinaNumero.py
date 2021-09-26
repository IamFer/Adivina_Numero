# Reto 01 - Adivina en que numero estoy pensando - Martínez Cruz Fernando Amador
import random, time, os

from Colores import Color
from Sonidos import Reproducir

intervalo = [1, 100]
historial = []
numero_pensado = random.randint(intervalo[0], intervalo[1])

Reproducir.INICIO.play()
print(Color.AZUL + "===============================================================================\n"+
      "¡Bienvenido Humano! Si deseas continuar navegando, tendras que completar\neste desafio: \n\n"+
      "Para pasar, tendras que adivinar el numero en el que estoy pensando\n"+
      "Pero mira, hoy estoy de buenas, y te dire que tan cercano estas del numero, \n"+
      "y como eres solo un humano, solo pensare en un intervalo del 1 al 100.\n\n"+
      "Si logras adivinar el numero en el que estoy pensando, al primer intento, \nte dare una recompensa.\n"+
      "¡Suerte Humano!\n"+
      "===============================================================================" + Color.REINICIADO)

while (mi_numero := input("\nEl número pensado esta entre "+str(intervalo)+", adivina: \n")) != str(numero_pensado):
    Reproducir.ERROR.play()

    if mi_numero.isdigit():
        mi_numero = int(mi_numero)
    else:
        print(Color.ROJO + "¡CUIDADO! Esto no es un numero entero. Trata de nuevo." + Color.REINICIADO)
        continue

    if mi_numero < intervalo[1] and mi_numero > numero_pensado:
        intervalo[1] = mi_numero
    elif mi_numero > intervalo[0] and mi_numero < numero_pensado:
        intervalo[0] = mi_numero

    historial.append(mi_numero)

historial.append(mi_numero)
os.system("cls")

print(Color.VERDE + "\n¡FELICIDADES!" + Color.REINICIADO + " Lograste adivinar en el intento " + str(len(historial)) + ".")
print("Tu recompensa es el poder de creer mas en ti y no dudar de ello. No lo olvides crack :3 (No habia recompensa xd)" if len(historial) < 2 else "")
print("Tu historial es " + str(historial))
print(Color.AZUL + "\nMe despido humano, puedes seguir navegando, y hazlo de manera segura. Mi ultimo mensaje antes de desaparecer. Adios.\n\n -Sr Computador." + Color.REINICIADO)

Reproducir.LOGRADO.play()
time.sleep(5)