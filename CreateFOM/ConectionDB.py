import pyodbc

class ConexionSQLServer:
    def __init__(self):
        self.server = '172.20.10.227'
        self.database = 'DBCMACICA'
        self.username = 'optimus'
        self.password = 'optimus'
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
            print("Conexión exitosa.")
        except Exception as e:
            print("Error al conectar a la base de datos:", e)

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")

    def obtener_nombre_persona(self, cUser):
        if not self.conexion:
            print("No hay conexión establecida.")
            return None

        try:
            cursor = self.conexion.cursor()
            consulta = "select dbo.FN_ObtieneNombreCompletoPersona(cPersCod,0) from rrhh where nRHEstado = 201 and cUser = ?"
            cursor.execute(consulta, (cUser,))
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                return resultado[0]
            else:
                print("No se encontró ninguna persona con ese ID.")
                return None
        except Exception as e:
            print("Error al obtener el nombre de la persona:", e)
            return None


class Consultas:
    def consultar_cuser (self, cUser):
        conexion = ConexionSQLServer()
        conexion.conectar()
        cUser=conexion.obtener_nombre_persona(cUser)
        conexion.desconectar()
        return cUser

 # Ejemplo de uso
        #conexion = ConexionSQLServer('172.20.10.227', 'DBCMACICA', 'optimus', 'optimus')
# conexion = ConexionSQLServer()
# conexion.conectar()
#
# nombre = conexion.obtener_nombre_persona(cUser)
# if nombre:
#     print("El nombre de la persona es:", nombre)
# conexion.desconectar()


