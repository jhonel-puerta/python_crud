import pymysql

class Connection:
    def __init__(self):
        self.servidor= "localhost"
        self.bd="ION_SAC"
        self.usuario="root"
        self.clave=""

    def conectar(self):
        try:
            self.conexion = pymysql.connect(self.servidor, self.usuario, self.clave, self.bd)
            self.cn = self.conexion.cursor()
            print("se conectó a la base de datos")

        except Exception as e:
            print("error al conectarse", e)

    def setEjecutarQuery(self,sql):
        try:
            respuesta = self.cn.execute(sql)
            print("respuesta: ",respuesta)
            self.conexion.commit()
            self.conexion.close()
            return 1
        except Exception as ex:
            print("error: ",ex)
            self.conexion.rollback()
            return 0


    def getEjecutarQuery(self,sql):
        try:
            self.cn.execute(sql)
            registro = self.cn.fetchall()
            return registro
        except Exception as ex:
            print("error: ", ex)
            return 0
