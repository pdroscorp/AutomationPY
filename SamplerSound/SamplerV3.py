import os
import keyboard
import pygame
import threading

# Ruta de la carpeta que contiene los archivos de sonido
carpeta_sonidos = "C:/Users/plpq/Music/EFECTOS/"

# Diccionario que mapeará teclas a archivos de sonido
sonidos = {}

def cargar_sonidos_desde_carpeta(ruta_carpeta):
    # Recorrer la carpeta y agregar los archivos de sonido al diccionario sonidos
    for indice, archivo in enumerate(os.listdir(ruta_carpeta)):
        if archivo.endswith(".wav") or archivo.endswith(".mp3"):  # Asegurarse de que sean archivos .wav
            tecla_asignada = str(indice + 1)  # Índice correlativo (empezando desde 1)
            nombre_archivo = os.path.join(ruta_carpeta, archivo)
            sonidos[tecla_asignada] = nombre_archivo
            print(f"{tecla_asignada}: {archivo}")

def reproducir_sonido(nombre_archivo):
    pygame.mixer.music.load(nombre_archivo)
    pygame.mixer.music.play()

def detectar_teclas_sonido():
    while True:
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN and evento.name in sonidos:
            nombre_archivo = sonidos[evento.name]
            reproducir_sonido(nombre_archivo)

if __name__ == "__main__":
    # Inicializar Pygame para reproducir sonidos
    pygame.mixer.init()
    print("Cargando sonidos desde la carpeta:")
    cargar_sonidos_desde_carpeta(carpeta_sonidos)
    # Crear un hilo para detectar las teclas y reproducir sonidos
    hilo_detencion = threading.Thread(target=detectar_teclas_sonido)
    hilo_detencion.start()

    # Mantener el programa principal activo
    try:
        hilo_detencion.join()
    except KeyboardInterrupt:
        # Manejar la interrupción del teclado para terminar el programa
        pygame.mixer.music.stop()
        pygame.mixer.quit()
