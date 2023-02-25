from subprocess import call
import os

print("========PORT FORWARD CONFIGURATIONS========")
os.system("oc get projects")
print("===========================================")
print ("Seleccione:")
diccionario =  {1:"bot", 2:"box", 3:"ftc", 4:"gen", 5:"hbc", 6:"pwp"}
MS=input(str(diccionario) + " :")
#os.system("oc port-forward service/box-configurations 8083:8888")

os.system("oc project " + diccionario[int(MS)] + "-cmacica-qa")
print ("======================================================================================")
print ("SE EJECUTÓ EL COMANDO:")
print ("--------------------------------------------------------------------------------------")
print ("> oc port-forward service/"+diccionario[int(MS)]+"-configurations 8083:8888")
print ("======================================================================================")
#direccion = "C:/Users/plpq/AppData/Local/Postman/"
#os.system(direccion + 'Postman.exe')
call(["C:/Users/plpq/AppData/Local/Postman/Postman.exe"])
os.system("oc port-forward service/"+diccionario[int(MS)]+"-configurations 8083:8888")

