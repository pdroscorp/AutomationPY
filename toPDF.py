#py -m pip install docx2pdf
import os
import docx2pdf
import sys
def convertir_docx_a_pdf(carpeta):
    # Obtener la lista de archivos .docx en la carpeta
    archivos_docx = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.docx')]

    if not archivos_docx:
        print("No se encontraron archivos .docx en la carpeta.")
        return
    print(f"===Se encontraron {len(archivos_docx)} archivos .docx en la carpeta===\n")
    # Mostrar la lista de archivos uno por uno mientras se convierten a PDF
    for archivo in archivos_docx:
        print(f"-> Convirtiendo {archivo} a PDF...")
        try:
            docx2pdf.convert(os.path.join(carpeta, archivo))
            print(f"{archivo} convertido exitosamente.\n")
        except Exception as e:
            print(f"Error al convertir {archivo}: {str(e)}")

#if __name__ == "__main__":
if len(sys.argv) > 1:
    parametro = sys.argv[1]
    convertir_docx_a_pdf(parametro)
else:
    print("No se proporcionó la ruta actual como argumento.")


"""
import sys
import os.path
def obtener_extensiones_en_carpeta(ruta_carpeta):
    extensiones = set()

    # Verificar si la ruta es una carpeta válida
    if not os.path.isdir(ruta_carpeta):
        return extensiones

    # Recorrer los archivos en la carpeta
    for archivo in os.listdir(ruta_carpeta):
        # Obtener la extensión del archivo
        extension = os.path.splitext(archivo)[1]
        # Agregar la extensión a la lista
        if extension:
            extensiones.add(extension)

    return extensiones

if len(sys.argv) > 1:
    parametro = sys.argv[1]
    print(f"El parámetro recibido es: {parametro}")
else:
    print("No se proporcionó la ruta actual como argumento.")


extensiones = obtener_extensiones_en_carpeta(parametro)

if extensiones:
    print("Extensiones encontradas en la carpeta:")
    for extension in extensiones:
        print(extension)
else:
    print("No se encontraron extensiones en la carpeta.")"""
