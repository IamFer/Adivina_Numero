import os, pygame # Importaremos un modulo externo, en este caso pygame para poder reproducir los sonidos durante la ejecucion

pygame.mixer.init()

INICIO = pygame.mixer.Sound("Sonidos/Inicio.wav")
ERROR = pygame.mixer.Sound("Sonidos/Error.wav")
LOGRADO = pygame.mixer.Sound("Sonidos/Logrado.wav")

os.system("cls")