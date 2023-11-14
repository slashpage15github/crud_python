import model.package_model.Database as Database
class Empresa:
    def __init__(self, id_empresa='', nombre_empresa=''):
        self.__id_empresa=id_empresa
        self.__nombre_empresa=nombre_empresa
    
    def obtener_empresas(self):
        conexion = Database.Database()
        empresas = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_EMPRESA,NOMBRE_EMPRESA FROM empresa")
            empresas = cursor.fetchall()
        conexion.conn.close()
        return empresas
    
    def obtener_empresa_por_id(self,id):
        conexion = conexion = Database.Database()
        empresa = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT ID_EMPRESA,NOMBRE_EMPRESA FROM empresa WHERE ID_EMPRESA = %s", (id))
            empresa = cursor.fetchone()
        conexion.conn.close()
        return empresa                