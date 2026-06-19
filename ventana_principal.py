# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDoubleSpinBox, QFormLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutMain = QVBoxLayout(self.centralwidget)
        self.layoutMain.setSpacing(10)
        self.layoutMain.setObjectName(u"layoutMain")
        self.layoutMain.setContentsMargins(16, 16, 16, 16)
        self.groupCliente = QGroupBox(self.centralwidget)
        self.groupCliente.setObjectName(u"groupCliente")
        self.formCliente = QFormLayout(self.groupCliente)
        self.formCliente.setObjectName(u"formCliente")
        self.formCliente.setContentsMargins(10, 10, 10, 10)
        self.lblNombre = QLabel(self.groupCliente)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formCliente.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.lineNombre = QLineEdit(self.groupCliente)
        self.lineNombre.setObjectName(u"lineNombre")

        self.formCliente.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineNombre)

        self.lblTelefono = QLabel(self.groupCliente)
        self.lblTelefono.setObjectName(u"lblTelefono")

        self.formCliente.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTelefono)

        self.lineTelefono = QLineEdit(self.groupCliente)
        self.lineTelefono.setObjectName(u"lineTelefono")

        self.formCliente.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineTelefono)

        self.lblCorreo = QLabel(self.groupCliente)
        self.lblCorreo.setObjectName(u"lblCorreo")

        self.formCliente.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCorreo)

        self.lineCorreo = QLineEdit(self.groupCliente)
        self.lineCorreo.setObjectName(u"lineCorreo")

        self.formCliente.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineCorreo)

        self.lblCodigoCliente = QLabel(self.groupCliente)
        self.lblCodigoCliente.setObjectName(u"lblCodigoCliente")

        self.formCliente.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblCodigoCliente)

        self.lineCodigoCliente = QLineEdit(self.groupCliente)
        self.lineCodigoCliente.setObjectName(u"lineCodigoCliente")
        self.lineCodigoCliente.setReadOnly(True)

        self.formCliente.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineCodigoCliente)


        self.layoutMain.addWidget(self.groupCliente)

        self.groupPedido = QGroupBox(self.centralwidget)
        self.groupPedido.setObjectName(u"groupPedido")
        self.layoutPedido = QVBoxLayout(self.groupPedido)
        self.layoutPedido.setObjectName(u"layoutPedido")
        self.layoutPedido.setContentsMargins(10, 10, 10, 10)
        self.formPedidoBase = QFormLayout()
        self.formPedidoBase.setObjectName(u"formPedidoBase")
        self.lblCodigo = QLabel(self.groupPedido)
        self.lblCodigo.setObjectName(u"lblCodigo")

        self.formPedidoBase.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblCodigo)

        self.lineCodigo = QLineEdit(self.groupPedido)
        self.lineCodigo.setObjectName(u"lineCodigo")
        self.lineCodigo.setReadOnly(True)

        self.formPedidoBase.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineCodigo)

        self.lblTotalIVA = QLabel(self.groupPedido)
        self.lblTotalIVA.setObjectName(u"lblTotalIVA")

        self.formPedidoBase.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTotalIVA)

        self.spinTotalIVA = QDoubleSpinBox(self.groupPedido)
        self.spinTotalIVA.setObjectName(u"spinTotalIVA")
        self.spinTotalIVA.setMinimum(0.000000000000000)
        self.spinTotalIVA.setMaximum(999999.989999999990687)
        self.spinTotalIVA.setDecimals(2)

        self.formPedidoBase.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinTotalIVA)


        self.layoutPedido.addLayout(self.formPedidoBase)

        self.layoutTipo = QHBoxLayout()
        self.layoutTipo.setObjectName(u"layoutTipo")
        self.lblTipo = QLabel(self.groupPedido)
        self.lblTipo.setObjectName(u"lblTipo")

        self.layoutTipo.addWidget(self.lblTipo)

        self.radioDomicilio = QRadioButton(self.groupPedido)
        self.radioDomicilio.setObjectName(u"radioDomicilio")
        self.radioDomicilio.setChecked(True)

        self.layoutTipo.addWidget(self.radioDomicilio)

        self.radioMesa = QRadioButton(self.groupPedido)
        self.radioMesa.setObjectName(u"radioMesa")

        self.layoutTipo.addWidget(self.radioMesa)

        self.spacerTipo = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutTipo.addItem(self.spacerTipo)


        self.layoutPedido.addLayout(self.layoutTipo)

        self.stackedWidget = QStackedWidget(self.groupPedido)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageDomicilio = QWidget()
        self.pageDomicilio.setObjectName(u"pageDomicilio")
        self.formDomicilio = QFormLayout(self.pageDomicilio)
        self.formDomicilio.setObjectName(u"formDomicilio")
        self.lblRecargo = QLabel(self.pageDomicilio)
        self.lblRecargo.setObjectName(u"lblRecargo")

        self.formDomicilio.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblRecargo)

        self.spinRecargo = QDoubleSpinBox(self.pageDomicilio)
        self.spinRecargo.setObjectName(u"spinRecargo")
        self.spinRecargo.setMinimum(0.000000000000000)
        self.spinRecargo.setMaximum(999999.989999999990687)
        self.spinRecargo.setDecimals(2)

        self.formDomicilio.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinRecargo)

        self.stackedWidget.addWidget(self.pageDomicilio)
        self.pageMesa = QWidget()
        self.pageMesa.setObjectName(u"pageMesa")
        self.formMesa = QFormLayout(self.pageMesa)
        self.formMesa.setObjectName(u"formMesa")
        self.lblServicio = QLabel(self.pageMesa)
        self.lblServicio.setObjectName(u"lblServicio")

        self.formMesa.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblServicio)

        self.spinServicio = QDoubleSpinBox(self.pageMesa)
        self.spinServicio.setObjectName(u"spinServicio")
        self.spinServicio.setMinimum(0.000000000000000)
        self.spinServicio.setMaximum(999999.989999999990687)
        self.spinServicio.setDecimals(2)

        self.formMesa.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinServicio)

        self.stackedWidget.addWidget(self.pageMesa)

        self.layoutPedido.addWidget(self.stackedWidget)


        self.layoutMain.addWidget(self.groupPedido)

        self.btnAgregar = QPushButton(self.centralwidget)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setMinimumHeight(36)

        self.layoutMain.addWidget(self.btnAgregar)

        self.groupPedidos = QGroupBox(self.centralwidget)
        self.groupPedidos.setObjectName(u"groupPedidos")
        self.layoutTabla = QVBoxLayout(self.groupPedidos)
        self.layoutTabla.setObjectName(u"layoutTabla")
        self.layoutTabla.setContentsMargins(10, 10, 10, 10)
        self.tablaPedidos = QTableWidget(self.groupPedidos)
        if (self.tablaPedidos.columnCount() < 6):
            self.tablaPedidos.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaPedidos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaPedidos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaPedidos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaPedidos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaPedidos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaPedidos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tablaPedidos.setObjectName(u"tablaPedidos")
        self.tablaPedidos.setMinimumHeight(160)
        self.tablaPedidos.setColumnCount(6)
        self.tablaPedidos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaPedidos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaPedidos.horizontalHeader().setStretchLastSection(True)

        self.layoutTabla.addWidget(self.tablaPedidos)


        self.layoutMain.addWidget(self.groupPedidos)

        self.groupResumen = QGroupBox(self.centralwidget)
        self.groupResumen.setObjectName(u"groupResumen")
        self.layoutResumen = QHBoxLayout(self.groupResumen)
        self.layoutResumen.setObjectName(u"layoutResumen")
        self.layoutResumen.setContentsMargins(10, 10, 10, 10)
        self.layoutLabels = QVBoxLayout()
        self.layoutLabels.setObjectName(u"layoutLabels")
        self.lblCantidad = QLabel(self.groupResumen)
        self.lblCantidad.setObjectName(u"lblCantidad")

        self.layoutLabels.addWidget(self.lblCantidad)

        self.lblTotalGeneral = QLabel(self.groupResumen)
        self.lblTotalGeneral.setObjectName(u"lblTotalGeneral")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lblTotalGeneral.setFont(font)

        self.layoutLabels.addWidget(self.lblTotalGeneral)


        self.layoutResumen.addLayout(self.layoutLabels)

        self.spacerResumen = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutResumen.addItem(self.spacerResumen)

        self.layoutBotonesResumen = QVBoxLayout()
        self.layoutBotonesResumen.setObjectName(u"layoutBotonesResumen")
        self.btnCalcularTotal = QPushButton(self.groupResumen)
        self.btnCalcularTotal.setObjectName(u"btnCalcularTotal")

        self.layoutBotonesResumen.addWidget(self.btnCalcularTotal)

        self.btnLimpiar = QPushButton(self.groupResumen)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.layoutBotonesResumen.addWidget(self.btnLimpiar)


        self.layoutResumen.addLayout(self.layoutBotonesResumen)


        self.layoutMain.addWidget(self.groupResumen)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Restaurante", None))
        self.groupCliente.setTitle(QCoreApplication.translate("MainWindow", u"Datos del Cliente", None))
        self.lblNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lineNombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del cliente", None))
        self.lblTelefono.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.lineTelefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero de tel\u00e9fono", None))
        self.lblCorreo.setText(QCoreApplication.translate("MainWindow", u"Correo electr\u00f3nico:", None))
        self.lineCorreo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ejemplo@dominio.com", None))
        self.lblCodigoCliente.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo cliente:", None))
        self.lineCodigoCliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Se asigna autom\u00e1ticamente", None))
        self.lineCodigoCliente.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #f0f0f0; color: #555;", None))
        self.groupPedido.setTitle(QCoreApplication.translate("MainWindow", u"Datos del Pedido", None))
        self.lblCodigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.lineCodigo.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #f0f0f0; color: #555;", None))
        self.lblTotalIVA.setText(QCoreApplication.translate("MainWindow", u"Total (IVA incluido):", None))
        self.spinTotalIVA.setPrefix(QCoreApplication.translate("MainWindow", u"$ ", None))
        self.lblTipo.setText(QCoreApplication.translate("MainWindow", u"Tipo de pedido:", None))
        self.radioDomicilio.setText(QCoreApplication.translate("MainWindow", u"Domicilio", None))
        self.radioMesa.setText(QCoreApplication.translate("MainWindow", u"Mesa", None))
        self.lblRecargo.setText(QCoreApplication.translate("MainWindow", u"Recargo de entrega:", None))
        self.spinRecargo.setPrefix(QCoreApplication.translate("MainWindow", u"$ ", None))
        self.lblServicio.setText(QCoreApplication.translate("MainWindow", u"Cargo por servicio:", None))
        self.spinServicio.setPrefix(QCoreApplication.translate("MainWindow", u"$ ", None))
        self.btnAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar Pedido", None))
        self.groupPedidos.setTitle(QCoreApplication.translate("MainWindow", u"Pedidos Registrados", None))
        ___qtablewidgetitem = self.tablaPedidos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. Cliente", None))
        ___qtablewidgetitem1 = self.tablaPedidos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        ___qtablewidgetitem2 = self.tablaPedidos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. Pedido", None))
        ___qtablewidgetitem3 = self.tablaPedidos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        ___qtablewidgetitem4 = self.tablaPedidos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        ___qtablewidgetitem5 = self.tablaPedidos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.groupResumen.setTitle(QCoreApplication.translate("MainWindow", u"Resumen", None))
        self.lblCantidad.setText(QCoreApplication.translate("MainWindow", u"Pedidos registrados: 0", None))
        self.lblTotalGeneral.setText(QCoreApplication.translate("MainWindow", u"Total general: $ 0.00", None))
        self.btnCalcularTotal.setText(QCoreApplication.translate("MainWindow", u"Calcular Total", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar Todo", None))
    # retranslateUi

