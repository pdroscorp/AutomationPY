import os
import tkinter as tk
from tkinter import filedialog
import pygame
import keyboard
import threading
class SamplerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sampler")

        # Configuración de la carpeta de sonidos
        self.sound_folder = "C:/Users/plpq/Music/EFECTOS"
        self.sounds = self.load_sounds()

        # Configuración de la interfaz gráfica
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                index = i * 3 + j
                if index < len(self.sounds):
                    sound_name = os.path.splitext(os.path.basename(self.sounds[index]))[0]
                    button = tk.Button(root, width=10, height=5, bg="green", text=sound_name, command=lambda index=index: self.play_sound(index))
                    button.grid(row=i, column=j, padx=5, pady=5)
                    row.append(button)
            self.buttons.append(row)

        # Asignar eventos de teclado
        self.root.bind('<KeyPress>', self.key_pressed)

    def load_sounds(self):
        sounds = []
        for filename in os.listdir(self.sound_folder):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                sound_path = os.path.join(self.sound_folder, filename)
                sounds.append(sound_path)
        return sounds

    def play_sound(self, index):
        pygame.mixer.music.load(self.sounds[index])
        pygame.mixer.music.play()

    def key_pressed(self, event):
        # Convertir el número de la tecla a un índice
        try:
            key_index = int(event.char) - 1  # Restamos 1 porque los índices comienzan desde 0
            if 0 <= key_index < len(self.sounds):
                self.play_sound(key_index)
        except ValueError:
            pass  # Ignorar si la tecla presionada no es un número


def main():
    pygame.init()
    root = tk.Tk()
    app = SamplerApp(root)
    root.mainloop()

def detectar_tecla_combinada():
    # Combinación de teclas: Ctrl + Alt + 1
    activar_ventana = 'ctrl+alt+1'
    desactivar_ventana = 'ctrl+alt+0'
    sampler_activado = False
    while True:
        if not sampler_activado:
            # Esperar la combinación para activar el sampler
            keyboard.wait(activar_ventana)
            print("Sampler activado")
            sampler_activado = True
            main()
        else:
            keyboard.wait(desactivar_ventana)
            print("Sampler desactivado")
            sampler_activado = False

if __name__ == "__main__":
    pygame.mixer.init()

    # Crear un hilo para detectar las teclas y reproducir sonidos
    hilo_detencion = threading.Thread(target=detectar_tecla_combinada)
    hilo_detencion.start()

    # Mantener el programa principal activo
    try:
        hilo_detencion.join()
    except KeyboardInterrupt:
        # Manejar la interrupción del teclado para terminar el programa
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    #main()
