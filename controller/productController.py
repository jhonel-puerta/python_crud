from model.Product import *

class productController():
    def __init__(self):
        pass

    def crearRegistro(self,lista):
        self.enlace= product()
        self.enlace.crea_producto(lista[0],lista[1],lista[2],lista[3],lista[4])
        resp = self.enlace.agregarProducto()
        if(resp):
            print("registro correcto :))")
        else:
            print("registro incorrecto :(")

    def mostrarRegistro(self):
        n = product()
        listaProducts = n.mostrarProductos()
        return listaProducts

    def eliminarProducto(self,codigo):
        eliminar = product()
        resp = eliminar.eliminarProductos(codigo)
        if (resp):
            print("producto eliminado correctamente.",resp)
        else:
            print("error al eliminar",resp)
    def actualizarProducto(self,data):
        producto = product()
        resp = producto.actualizarProductos(data[0],data[1],data[2],data[3],data[4],data[5])
        print("el id ingresado es: ",data[0],"esta en el controller")
        if (resp):
            print("producto actualizado correctamente.")
        else:
            print("error al actualizar",resp)