# Dependencias necesarias
import shutil
import os
import datetime
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
rutaOrig = "D:/QA/INCIDENCIAS Y MEJORAS/"
rutaDest = "D:/QA/INCIDENCIAS Y MEJORAS/" + anio + "/"

# NOMBRE DEL FORMATO DE FOM
nameXLS = "_FOM_.xlsx"

# COPIA EL FOM  A LA RUTA DESTINO
shutil.copy(rutaOrig + nameXLS, rutaDest)
os.chdir(rutaDest)
if os.path.exists(nameXLS) == True :
    print("COPIADO")
else:
    print("ERROR AL COPIAR")


#print(os.getcwd())

os.rename(rutaDest+nameXLS,str(hoy)+" - "+tipoList[int(tipo)]+" - "+name+" - "+cuser+".xls")



#https://www.youtube.com/watch?v=KiDoIHAokZg
