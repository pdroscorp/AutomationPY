# Dependencias necesarias
import shutil
import os
import datetime
import openpyxl
# INICIO ---------

# INGRESO DE DATOS
tipo = input("Tipo : \n[1]Mejora \n[2]Incidencia \n[3]Requerimiento \n ->")
anio = input("Digita direccion de carpeta (AÑO)     :")
name = input("Digita nombre de mejora/incidencia    :")
cuser = input("Digita cUser del desarrollador        :")
detail = input("Digita Detalle del cambio             :")
hoy = datetime.date.today()

tipoList = {1:"Mejora",2:"Incidencia",3:"Requerimiento"}
# FIN INGRESO DE DATOS

# RUTA DE ORIGEN Y DESTINO PARA INCIDENCIAS Y MEJORAS
ruta = "D:/QA/INCIDENCIAS Y MEJORAS/"
rutaDest = "D:/QA/INCIDENCIAS Y MEJORAS/" + str(anio) + "/"
# NOMBRE DEL FORMATO DE FOM
nameXLS = "_FOM_.xlsx"

# COPIA EL FOM  A LA RUTA DESTINO
newName = str(hoy)+" - "+tipoList[int(tipo)]+" - "+name+" - "+cuser+".xlsx"
try:
    shutil.copy(ruta + nameXLS, rutaDest)
    os.chdir(rutaDest)
    # RENOMBRANDO EL ARCHIVO AL FORMATO:  FECHA-TIPO-NOMBRE-CUSER
    os.rename(rutaDest+nameXLS,newName)
    print("FOM GENERADO EN: " + rutaDest )
except shutil.SameFileError:
    print("ERROR AL COPIAR")

# MODIFICANDO EL EXCEL
url= rutaDest+newName

book = openpyxl.load_workbook(url)
sheet = book.active
#sheet ['C8'] = "00UIN3030"
sheet ['D8'] = name
sheet ['J8'] = datetime.date.today()
sheet ['I10'] = datetime.date.today()
sheet ['C13'] = cuser
os.chdir(rutaDest)
book.save(newName)
book.close()




print ("HA CONCLUIDO CON ÉXITO")



#https://www.youtube.com/watch?v=KiDoIHAokZg

# FIN ---------