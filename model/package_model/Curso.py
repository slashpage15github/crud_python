import model.package_model.Database as Database
class Curso:
    def __init__(self, id_curso=0, nombre_curso='',fecha_alta=''):
        self.__id_curso=id_curso
        self.__nombre_curso=nombre_curso
        self.__fecha_alta=fecha_alta

    def eliminar_curso(self,id):
        affected=0
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM catalogo_curso WHERE ID_CURSO = %s", (id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
        
    def insertar_cursos(self, obj_asp):
        #return obj_asp.__fecha_alta
        #return obj_asp
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO catalogo_curso(NOMBRE_CURSO,FECHA_ALTA) VALUES (%s, %s)"
                vals=(obj_asp.__nombre_curso,obj_asp.__fecha_alta)
                #return (query % vals) 
                affected=cursor.execute(query,vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
            finally:
                conexion.conn.close() 
    
    def obtener_cursos(self):
        conexion = Database.Database()
        cursos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_CURSO,NOMBRE_CURSO,FECHA_ALTA FROM catalogo_curso")
            cursos = cursor.fetchall()
        conexion.conn.close()
        return cursos
    
    def obtener_curso_por_id(self,id):
        conexion = conexion = Database.Database()
        curso = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_CURSO,NOMBRE_CURSO,FECHA_ALTA FROM catalogo_curso WHERE ID_CURSO = %s", (id))
            curso = cursor.fetchone()
        conexion.conn.close()
        return curso                