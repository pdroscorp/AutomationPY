# Dependencias necesarias

import shutil
import os
import datetime
import openpyxl #pip install openpyxl


# Ruta del directorio que deseas abrir
ruta_directorio = "D:/QA/INCIDENCIAS Y MEJORAS/2024/2024-04-25 - Incidencia - Inc test - AGAF/"
print (ruta_directorio)
# Verificar si la ruta es un directorio válido
if os.path.isdir(ruta_directorio):
    # Abrir el directorio en el explorador de archivos del sistema
    os.system(f'start "DIRECTORIO" "{ruta_directorio}"')
else:
    print("La ruta no es un directorio válido.")



#https://www.youtube.com/watch?v=KiDoIHAokZg

# FIN ---------