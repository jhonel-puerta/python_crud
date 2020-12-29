from controller.productController import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)

class crear(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dialog/crear.ui", self)
        self.setWindowTitle("Crear")
        self.pushButton.clicked.connect(self.crear)

    def crear(self):
        codigo = self.inputCodigo.text()
        nombre = self.inputNombre.text()
        categoria = self.comboBoxCategoria.currentText()
        unidades = self.spinBoxUnidades.value()
        precio = self.spinBoxPrecio.value()

        product_data = [codigo, nombre , categoria,str(unidades), str(precio)]
        lazo = productController()
        lazo.crearRegistro(product_data)

class actualizar(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dialog/actualizar.ui", self)
        self.setWindowTitle("Actualizar")
        #buttons
        self.buttonActualizar.clicked.connect(self.actualiza)
        self.buttonBuscar.clicked.connect(self.mostrar_datos)
        self.enlace = productController()


    def actualiza(self):
        self.productCode = self.inputCodigoProducto.text()
        codigo = self.inputCodigo.text()
        nombre = self.inputNombre.text()
        categoria = self.inputCategoria.text()
        unidades = self.inputUnidades.text()
        precio = self.inputPrecio.text()

        data = Main()
        data.mostrarProductos()

        product_data_actualizar = [self.productCode, str(codigo), nombre, categoria, str(unidades), str(precio)]
        self.enlace.actualizarProducto(product_data_actualizar)

    def mostrar_datos(self):
        datos = productController()
        lista_datos = datos.mostrarRegistro()
        listaCodigos = []
        for i in range(len(lista_datos)):
            listaCodigos.append(lista_datos[i][0])
        print(listaCodigos)
        code = self.inputCodigoProducto.text()
        if code in listaCodigos:
            codigo = lista_datos[listaCodigos.index(code)][0]
            nombre = lista_datos[listaCodigos.index(code)][1]
            categoria = lista_datos[listaCodigos.index(code)][2]
            unidades = lista_datos[listaCodigos.index(code)][3]
            precio = lista_datos[listaCodigos.index(code)][4]

            self.inputCodigo.setText(codigo)
            self.inputNombre.setText(nombre)
            self.inputCategoria.setText(categoria)
            self.inputUnidades.setText(unidades)
            self.inputPrecio.setText(str(precio))

        else:
            print("losientobb")

class eliminar(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dialog/eliminar.ui", self)
        self.setWindowTitle("Eliminar")

        self.buttonEliminar.clicked.connect(self.eliminar)
    def eliminar(self):
        enlace = productController()
        enlace.eliminarProducto(self.inputCodigoEliminar.text())

class Main(QMainWindow,QDialog,QTableWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui",self)
        self.setWindowTitle("PANEL DE CONTROL ION SAC")
        self.ButtonNew.clicked.connect(self.abrirVentanaCrear)
        self.ButtonEdit.clicked.connect(self.abrirVentanaActualizar)
        self.ButtonDelete.clicked.connect(self.abrirVentanaEliminar)
        self.ButtonBuscar.clicked.connect(self.buscarProducto)
        self.btnMostrar.clicked.connect(self.mostrarProductos)


        # ================== WIDGET  QTableWidget ==================

        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setDragDropOverwriteMode(False)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.setTextElideMode(Qt.ElideRight)
        self.tabla.setWordWrap(False)
        self.tabla.setSortingEnabled(False)
        self.tabla.setRowCount(0)
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                          Qt.AlignCenter)

        self.tabla.horizontalHeader().setHighlightSections(False)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setAlternatingRowColors(True)
        #altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)

        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)
    def buscarProducto(self):
        pass

    def mostrarProductos(self):
        self.tabla.setColumnCount(5)
        columnas = ("Codigo", "Nombre", "Categoria", "Unidades", "Precio")
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(columnas)
        self.tabla.clearContents()
        self.tabla.setRowCount(0)
        fila = 0
        DatosRegistro = productController().mostrarRegistro()
        for registro in DatosRegistro:
            columna = 0
            self.tabla.insertRow(fila)
            for elemento in registro:
                element = str(elemento)
                celda = QTableWidgetItem(element)
                self.tabla.setItem(fila,columna,celda)
                print(elemento)
                columna += 1
            fila += 1

    def abrirVentanaCrear(self):
        dialogo = crear()
        dialogo.show()
        dialogo.exec_()
    def abrirVentanaActualizar(self):
        dialogo = actualizar()
        dialogo.show()
        dialogo.exec_()
    def abrirVentanaEliminar(self):
        dialogo = eliminar()
        dialogo.show()
        dialogo.exec_()


app = QApplication(sys.argv)
GUI = Main()
GUI.show()
sys.exit(app.exec_())