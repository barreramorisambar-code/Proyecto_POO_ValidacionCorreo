import sys
import os

from PySide6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader

from dominio.cliente import Cliente, PATRON_CORREO
from dominio.pedido_domicilio import PedidoDomicilio
from dominio.pedido_mesa import PedidoMesa
from dominio.gestor_pedidos import GestorPedidos


class VentanaPrincipal:

    def __init__(self):
        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "GUI/ventana_principal.ui")
        archivo_ui = QFile(ui_path)
        archivo_ui.open(QFile.ReadOnly)
        self.ui = loader.load(archivo_ui)
        archivo_ui.close()

        self._gestor = GestorPedidos()
        self._lista_pedidos = []
        self._registro_clientes = {}   # telefono -> {"codigo": "CLI-001", "objeto": Cliente}
        self._contador_clientes = 0
        self._contador_mesa = 0
        self._contador_domicilio = 0

        self._configurar_tabla()
        self._conectar_senales()
        self._actualizar_preview_codigo()

    def _configurar_tabla(self):
        tabla = self.ui.tablaPedidos
        tabla.horizontalHeader().setStretchLastSection(True)
        tabla.setColumnWidth(0, 90)   # Cód. Cliente
        tabla.setColumnWidth(1, 90)   # Tipo
        tabla.setColumnWidth(2, 90)   # Cód. Pedido
        tabla.setColumnWidth(3, 150)  # Cliente
        tabla.setColumnWidth(4, 110)  # Teléfono
        tabla.setColumnWidth(5, 90)   # Total

    def _conectar_senales(self):
        self.ui.btnAgregar.clicked.connect(self._agregar_pedido)
        self.ui.btnCalcularTotal.clicked.connect(self._calcular_total)
        self.ui.btnLimpiar.clicked.connect(self._limpiar_todo)
        self.ui.radioDomicilio.toggled.connect(self._cambiar_tipo)
        self.ui.lineTelefono.textChanged.connect(self._buscar_cliente_existente)

    def show(self):
        self.ui.show()

    # ── Registro de clientes ──────────────────────────────────────────────────

    def _buscar_cliente_existente(self, telefono):
        telefono = telefono.strip()
        if telefono in self._registro_clientes:
            datos = self._registro_clientes[telefono]
            self.ui.lineCodigoCliente.setText(datos["codigo"])
            self.ui.lineNombre.setText(datos["objeto"].nombre)
            self.ui.lineCorreo.setText(datos["objeto"].correo)
        else:
            self.ui.lineCodigoCliente.setText("")

    def _obtener_o_crear_cliente(self, nombre, telefono, correo):
        if telefono in self._registro_clientes:
            return self._registro_clientes[telefono]["objeto"], self._registro_clientes[telefono]["codigo"]
        self._contador_clientes += 1
        codigo = f"CLI-{self._contador_clientes:03d}"
        cliente = Cliente(nombre, telefono, correo)
        self._registro_clientes[telefono] = {"codigo": codigo, "objeto": cliente}
        return cliente, codigo

    # ── Tipo de pedido ────────────────────────────────────────────────────────

    def _cambiar_tipo(self, domicilio_activo):
        self.ui.stackedWidget.setCurrentIndex(0 if domicilio_activo else 1)
        self._actualizar_preview_codigo()

    def _actualizar_preview_codigo(self):
        if self.ui.radioDomicilio.isChecked():
            self.ui.lineCodigo.setText(f"DOM-{self._contador_domicilio + 1:03d}")
        else:
            self.ui.lineCodigo.setText(f"MESA-{self._contador_mesa + 1:03d}")

    # ── Agregar pedido ────────────────────────────────────────────────────────

    def _agregar_pedido(self):
        nombre = self.ui.lineNombre.text().strip()
        telefono = self.ui.lineTelefono.text().strip()
        correo = self.ui.lineCorreo.text().strip()
        total_iva = self.ui.spinTotalIVA.value()

        if not nombre or not telefono or not correo:
            QMessageBox.warning(self.ui, "Campos vacíos",
                                "Completa nombre, teléfono y correo antes de agregar.")
            return
        if len(telefono) != 10:
            QMessageBox.warning(self.ui, "Telefono inválido", "Debe de contener exactamente 10 caracteres")
            return
        if not PATRON_CORREO.match(correo):
            QMessageBox.warning(self.ui, "Correo inválido",
                                "El correo electrónico ingresado no tiene un formato válido.\n"
                                "Ejemplo correcto: usuario@dominio.com")
            self.ui.lineCorreo.setFocus()
            return
        cliente, cod_cliente = self._obtener_o_crear_cliente(nombre, telefono, correo)
        self.ui.lineCodigoCliente.setText(cod_cliente)

        if self.ui.radioDomicilio.isChecked():
            self._contador_domicilio += 1
            codigo = f"DOM-{self._contador_domicilio:03d}"
            recargo = self.ui.spinRecargo.value()
            pedido = PedidoDomicilio(codigo, cliente, total_iva, recargo)
            tipo_texto = "Domicilio"
        else:
            self._contador_mesa += 1
            codigo = f"MESA-{self._contador_mesa:03d}"
            servicio = self.ui.spinServicio.value()
            pedido = PedidoMesa(codigo, cliente, total_iva, servicio)
            tipo_texto = "Mesa"

        self._lista_pedidos.append(pedido)
        self._agregar_fila_tabla(tipo_texto, pedido, cliente, cod_cliente)
        self._actualizar_cantidad()
        QMessageBox.information(self.ui, "Pedido registrado",
                                f"Pedido {pedido.codigo} agregado correctamente para {cliente.correo}.")
        self._limpiar_formulario()
        self._actualizar_preview_codigo()

    def _agregar_fila_tabla(self, tipo_texto, pedido, cliente, cod_cliente):
        tabla = self.ui.tablaPedidos
        fila = tabla.rowCount()
        tabla.insertRow(fila)

        tabla.setItem(fila, 0, self._celda(cod_cliente))
        tabla.setItem(fila, 1, self._celda(tipo_texto))
        tabla.setItem(fila, 2, self._celda(pedido.codigo))
        tabla.setItem(fila, 3, self._celda(cliente.nombre))
        tabla.setItem(fila, 4, self._celda(cliente.telefono))
        tabla.setItem(fila, 5, self._celda(f"$ {pedido.calcular_total():.2f}"))

    def _celda(self, texto):
        item = QTableWidgetItem(str(texto))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    # ── Calcular total ────────────────────────────────────────────────────────

    def _calcular_total(self):
        if not self._lista_pedidos:
            QMessageBox.warning(self.ui, "Sin pedidos", "No existen pedidos para calcular.")
            return
        total = self._gestor.calcular_total_pedidos(self._lista_pedidos)
        self.ui.lblTotalGeneral.setText(f"Total general: $ {total:.2f}")

    # ── Limpiar ───────────────────────────────────────────────────────────────

    def _limpiar_todo(self):
        self._lista_pedidos.clear()
        self._registro_clientes.clear()
        self._contador_clientes = 0
        self._contador_mesa = 0
        self._contador_domicilio = 0
        self.ui.tablaPedidos.setRowCount(0)
        self.ui.lblCantidad.setText("Pedidos registrados: 0")
        self.ui.lblTotalGeneral.setText("Total general: $ 0.00")
        self._limpiar_formulario()
        self._actualizar_preview_codigo()

    def _limpiar_formulario(self):
        self.ui.lineNombre.clear()
        self.ui.lineTelefono.clear()
        self.ui.lineCorreo.clear()
        self.ui.lineCodigoCliente.clear()
        self.ui.spinTotalIVA.setValue(0.0)
        self.ui.spinRecargo.setValue(0.0)
        self.ui.spinServicio.setValue(0.0)
        self.ui.lineNombre.setFocus()

    def _actualizar_cantidad(self):
        n = len(self._lista_pedidos)
        self.ui.lblCantidad.setText(f"Pedidos registrados: {n}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
