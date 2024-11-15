# Dependencias necesarias
import shutil
import os
import datetime
import openpyxl #pip install openpyxl

# INICIO ---------

from ConectionDB import Consultas
test = Consultas()
nombre=test.consultar_cuser('PLPQ')
print(nombre)



# INGRESO DE DATOS

tipoList = {1:"Mejora",2:"Incidencia",3:"Requerimiento"}
undList = {1:"UBI",2:"UBO",3:"UCE",4:"UCR",5:"UFC",6:"UIN",7:"UOP"}

tipo =      input("Tipo : \n[1]Mejora \n[2]Incidencia \n[3]Requerimiento \n ->")
if tipo=="3":
    print("Unidad de desarrollo:")
    unidad =      input("Tipo :     \n[1]UBI   [2]UBO   [3]UCE   [4]UCR \n[5]UFC   [6]UIN   [7]UOP   \n ->")
    codigorq =      input("Código de Requerimiento: ")

print("Descripción:")
anio =      input("Direccion de carpeta (AÑO)   :")
name =      input("Nombre de "+tipoList[int(tipo)]+":")
cuser =     input("cUser del desarrollador      :")
detail =    input("Detalle del cambio           :")
hoy = datetime.date.today()

# FIN INGRESO DE DATOS

# RUTA DE FOM Y NOMBRE DE FORMATO DE FOM
rutaFOM = "D:/QA/INCIDENCIAS Y MEJORAS/"
nameXLS = "_FOM____ULTIMO.xlsx"
# RUTA DE ORIGEN Y DESTINO PARA INCIDENCIAS Y MEJORAS
rutaDestIM = "D:/QA/INCIDENCIAS Y MEJORAS/"
# RUTA DE ORIGEN Y DESTINO PARA REQUERIMIENTOS
rutaDestReq = "D:/QA/REQUERIMIENTOS/"

# COPIA EL FOM  A LA RUTA DESTINO
rutaDest = ""
newName = ""
if tipo == "3":
    rutaDest = rutaDestReq + undList[int(unidad)] + "/" + str(anio) + "/"
    newName = str(hoy)+" - "+codigorq+" - "+name+" - "+cuser
else:
    codigorq = "-"
    rutaDest = rutaDestIM + str(anio) + "/"
    newName = str(hoy)+" - "+tipoList[int(tipo)]+" - "+name+" - "+cuser
try:
    rutaFullDest = rutaDest + newName + "/"
    os.chdir(rutaDest)
    os.mkdir(newName)
    shutil.copy(rutaFOM + nameXLS, rutaDest+newName)
    os.chdir(rutaFullDest)
    # RENOMBRANDO EL ARCHIVO AL FORMATO:  FECHA-TIPO-NOMBRE-CUSER
    os.rename(rutaFullDest+nameXLS,newName+ ".xlsx")

    print("FOM GENERADO EN: " + rutaFullDest)
    if detail != "":
        # CREANDO ARCHIVO QUE MUESTRA EL DETALLE
        f = open(rutaFullDest+"Detalle.txt","w")
        f.write("Detalle:"+ detail)
        f.close()

except shutil.SameFileError:
    print("ERROR AL COPIAR")


    #echo %det% > "D:\QA\INCIDENCIAS Y MEJORAS\%ruta%\%ano%-%mes%-%dia% - Incidencia - %nombre% - %dev%\Detalle.txt"
# MODIFICANDO EL EXCEL
url= rutaFullDest+newName+".xlsx"
print(url)
book = openpyxl.load_workbook(url)
sheet = book.active
sheet ['C8'] = str(codigorq)
sheet ['D8'] = str(name)
sheet ['J8'] = datetime.date.today()
sheet ['I10'] = datetime.date.today()
sheet ['C13'] = str(cuser)
os.system(f'start "DIRECTORIO" "{rutaFullDest}"')
book.save(newName+".xlsx")
book.close()

print ("HA CONCLUIDO CON ÉXITO")

#https://www.youtube.com/watch?v=KiDoIHAokZg

# FIN ---------