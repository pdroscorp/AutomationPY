#pyinstaller --onefile Caver.py
#pyinstaller --onefile --add-data "Cave.exe;C:\Cave\Cave.exe" --add-data "secret.key;C:\Cave\secret.key" --icon cave_64.ico Install.py
import os
import winreg as reg

# Especifica la ruta que deseas agregar
ruta_install = r"C:/Cave"
def add_to_path(new_path):
    try:
        # Obtener la variable de entorno Path actual
        current_path = os.environ.get('Path', '')

        # Verificar si la ruta ya está en Path
        if new_path not in current_path:
            # Agregar la nueva ruta
            new_path = f"{current_path};{new_path}"

            # Actualizar la variable de entorno Path en el registro
            with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, reg.KEY_SET_VALUE) as key:
                reg.SetValueEx(key, 'Path', 0, reg.REG_EXPAND_SZ, new_path)
            print(f"La ruta '{new_path}' ha sido añadida a la variable de entorno Path.")
        else:
            print(f"La ruta '{new_path}' ya está en la variable de entorno Path.")

        # Crear el archivo .bat
        #create_bat_file(ruta_install)
        create_key_file(ruta_install)

    except PermissionError:
        print("Error: Necesita permisos de administrador para modificar la variable de entorno Path.")
        input("Presiona Enter para salir...")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def create_key_file(directory):
    os.makedirs(os.path.dirname(directory), exist_ok=True)  # Crea la carpeta si no existe
    file_path = os.path.join(directory, 'token.key')
    with open(file_path, 'w') as f:
        f.write(f"User: UserExample")
        f.write(f"Pass: T0k3n3x4mPl3")
    print(f"El archivo 'token.key' ha sido creado en  '{directory}'.")

##Aqui empieza
add_to_path(ruta_install)
# Pausa para ver el mensaje
input("Presiona Enter para continuar...")

#pyinstaller --onefile Install.py