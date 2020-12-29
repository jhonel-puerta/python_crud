from model.Connection import Connection

class product():

    def __init__(self):
        pass

    def crea_producto(self,codigo,nombre,categoria,unidades,precio):
        self.codigo=codigo
        self.nombre = nombre
        self.categoria = categoria
        self.unidades = unidades
        self.precio = precio

    def setCodigo(self,codigo):
        self.codigo=codigo
    def setNombre(self,nombre):
        self.nombre=nombre
    def setCategoria(self,categoria):
        self.categoria=categoria
    def setUnidades(self,unidades):
        self.unidades=unidades
    def setPrecio(self,precio):
        self.precio = precio

    def getCodgigo(self):
        return self.codigo
    def getNombre(self):
        return self.nombre
    def getCategoria(self):
        return self.categoria
    def getUnidades(self):
        return self.unidades
    def getPrecio(self):
        return self.precio


    def agregarProducto(self):
        conecta =Connection()
        conecta.conectar()
        SQL=  "INSERT INTO `productos` (`codigo`, `nombre`, `categoria`, `unidades`,`precio`) VALUES ('"+self.codigo+"','"+self.nombre+"','"+self.categoria+"','"+self.unidades+"','"+str(self.precio)+"')"
        print(SQL)
        resp= conecta.setEjecutarQuery(SQL)
        if (resp):
            return 1
        else:
            return 0
    def mostrarProductos(self):
        conecta = Connection()
        conecta.conectar()
        SQL = "SELECT * FROM productos"
        registros = conecta.getEjecutarQuery(SQL)
        return registros

    def eliminarProductos(self,codigo):
        conecta = Connection()
        conecta.conectar()
        SQL = "DELETE FROM `productos` WHERE `productos`.`codigo` = '"+str(codigo)+"'"
        elimina = conecta.setEjecutarQuery(SQL)
        if(SQL):
            return SQL
        else:
            return 0
    def actualizarProductos(self,cdp,codigo,nombre,categoria,unidades,precio):
        conecta =Connection()
        conecta.conectar()
        SQL = "UPDATE `productos` SET `codigo` = '"+codigo+"', `nombre` = '"+nombre+"', `categoria` = '"+categoria+"', `unidades` = '"+unidades+"', `precio` = '"+str(precio)+"' WHERE `productos`.`codigo` = '"+cdp+"'"
        actualiza = conecta.setEjecutarQuery(SQL)
        if (SQL):
            return 1
        else:
            return 0