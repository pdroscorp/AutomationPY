import os
import pyodbc
from colorama import Fore, Style
import shutil
def connect_to_database(server, database, username, password, driver='{SQL Server}'):
    """
    Conecta a la base de datos SQL Server.
    """
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(connection_string)

#Solo funciona para directorio principal
def convert_to_ansi(input_file, output_file):
    """
    Convierte un archivo de UTF-8 a ANSI.
    """
    with open(input_file, 'r', encoding='utf-8') as input:
        content = input.read()

    with open(output_file, 'w', encoding='ansi') as output:
        output.write(content)

#Funciona para directorio principal y subdirectorios
def get_procedure_files(directory):
    """
    Obtiene la lista de archivos de procedimientos almacenados en el directorio especificado y sus subdirectorios.
    """
    procedure_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.sql'):
                procedure_files.append(os.path.join(root, file))
    return procedure_files
def execute_procedure(connection, file_path):
    """
    Ejecuta un procedimiento almacenado desde un archivo en la base de datos.
    """
    with open(file_path, 'r') as file:
        procedure_content = file.read()

    cursor = connection.cursor()
    try:
        cursor.execute(procedure_content)
        #cursor.execute("EXECUTE sp_executesql N' [{}]".format(procedure_content))
        cursor.commit()
        print(f"{Fore.GREEN}Procedimiento almacenado en {file_path} ->>> ejecutado exitosamente.")
        return True
    except pyodbc.Error as e:
        print(f"{Fore.RED}Procedimiento almacenado en {file_path} ->>> ERROR: {e} ")
        error_directory = 'C:/Users/plpq/Documents/TEST/ERROR'
        os.makedirs(error_directory, exist_ok=True)
        shutil.copy(file_path, os.path.join(error_directory, os.path.basename(file_path)))
        return False
    finally:
        cursor.close()
def main():
    # Parámetros de conexión a la base de datos
    server = '172.20.10.227'
    database = 'DBCMACICA'
    username = 'optimus'
    password = 'optimus'

    # Directorio que contiene los archivos de procedimientos almacenados
    procedures_directory = 'C:/Users/plpq/Documents/TEST/Test2'

    # Conectar a la base de datos
    connection = connect_to_database(server, database, username, password)

    # Obtener la lista de archivos de procedimientos almacenados
    procedure_files = get_procedure_files(procedures_directory)
    files_failed = 0
    # Iterar sobre cada archivo de procedimiento almacenado y ejecutarlo
    for file_name in procedure_files:
        procedure_name = os.path.splitext(file_name)[0]
        file_path = os.path.join(procedures_directory, file_name)
        if execute_procedure(connection, file_path) is False:
            files_failed += 1

    print(f"{Fore.RED}Número de archivos que fallaron: {files_failed}{Style.RESET_ALL}")
    # Cerrar la conexión a la base de datos
    connection.close()

if __name__ == "__main__":
    main()
