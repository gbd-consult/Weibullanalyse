# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_weibullanalyse.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ValueWidgetBase(object):
    def setupUi(self, ValueWidgetBase):
        ValueWidgetBase.setObjectName("ValueWidgetBase")
        ValueWidgetBase.resize(366, 560)
        ValueWidgetBase.setMinimumSize(QtCore.QSize(366, 560))
        ValueWidgetBase.setMaximumSize(QtCore.QSize(366, 560))
        self.verticalLayout = QtWidgets.QVBoxLayout(ValueWidgetBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(ValueWidgetBase)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.InRastC = QtWidgets.QComboBox(ValueWidgetBase)
        self.InRastC.setMinimumSize(QtCore.QSize(200, 30))
        self.InRastC.setObjectName("InRastC")
        self.horizontalLayout_9.addWidget(self.InRastC)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(ValueWidgetBase)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.InRastK = QtWidgets.QComboBox(ValueWidgetBase)
        self.InRastK.setMinimumSize(QtCore.QSize(200, 30))
        self.InRastK.setObjectName("InRastK")
        self.horizontalLayout_7.addWidget(self.InRastK)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(ValueWidgetBase)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.InRastW = QtWidgets.QComboBox(ValueWidgetBase)
        self.InRastW.setMinimumSize(QtCore.QSize(200, 30))
        self.InRastW.setObjectName("InRastW")
        self.horizontalLayout_10.addWidget(self.InRastW)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(ValueWidgetBase)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.InRastZ = QtWidgets.QComboBox(ValueWidgetBase)
        self.InRastZ.setMinimumSize(QtCore.QSize(200, 30))
        self.InRastZ.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.InRastZ.setObjectName("InRastZ")
        self.horizontalLayout_6.addWidget(self.InRastZ)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbxActive = QtWidgets.QCheckBox(ValueWidgetBase)
        self.cbxActive.setMinimumSize(QtCore.QSize(0, 20))
        self.cbxActive.setObjectName("cbxActive")
        self.horizontalLayout_4.addWidget(self.cbxActive)
        self.cbxGraph = QtWidgets.QCheckBox(ValueWidgetBase)
        self.cbxGraph.setMinimumSize(QtCore.QSize(0, 20))
        self.cbxGraph.setStatusTip("")
        self.cbxGraph.setObjectName("cbxGraph")
        self.horizontalLayout_4.addWidget(self.cbxGraph)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(ValueWidgetBase)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dataName = QtWidgets.QLineEdit(ValueWidgetBase)
        self.dataName.setPlaceholderText("")
        self.dataName.setObjectName("dataName")
        self.horizontalLayout_5.addWidget(self.dataName)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.line_2 = QtWidgets.QFrame(ValueWidgetBase)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(ValueWidgetBase)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.bufferz0 = QtWidgets.QSpinBox(ValueWidgetBase)
        self.bufferz0.setMinimumSize(QtCore.QSize(0, 30))
        self.bufferz0.setMaximumSize(QtCore.QSize(16777215, 33))
        self.bufferz0.setMinimum(0)
        self.bufferz0.setMaximum(10000)
        self.bufferz0.setSingleStep(100)
        self.bufferz0.setProperty("value", 1500)
        self.bufferz0.setObjectName("bufferz0")
        self.horizontalLayout_11.addWidget(self.bufferz0)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(ValueWidgetBase)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 33))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.outputXEdit = QtWidgets.QTextEdit(ValueWidgetBase)
        self.outputXEdit.setMinimumSize(QtCore.QSize(0, 33))
        self.outputXEdit.setMaximumSize(QtCore.QSize(16777215, 33))
        self.outputXEdit.setObjectName("outputXEdit")
        self.horizontalLayout.addWidget(self.outputXEdit)
        self.label = QtWidgets.QLabel(ValueWidgetBase)
        self.label.setMaximumSize(QtCore.QSize(16777215, 33))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.outputYEdit = QtWidgets.QTextEdit(ValueWidgetBase)
        self.outputYEdit.setMinimumSize(QtCore.QSize(0, 33))
        self.outputYEdit.setMaximumSize(QtCore.QSize(16777215, 33))
        self.outputYEdit.setObjectName("outputYEdit")
        self.horizontalLayout.addWidget(self.outputYEdit)
        self.buttonSaveAs = QtWidgets.QPushButton(ValueWidgetBase)
        self.buttonSaveAs.setMinimumSize(QtCore.QSize(129, 33))
        self.buttonSaveAs.setMaximumSize(QtCore.QSize(16777215, 33))
        self.buttonSaveAs.setObjectName("buttonSaveAs")
        self.horizontalLayout.addWidget(self.buttonSaveAs)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graphControls = QtWidgets.QWidget(ValueWidgetBase)
        self.graphControls.setObjectName("graphControls")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.graphControls)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.graphControls)
        self.stackedWidget = QtWidgets.QStackedWidget(ValueWidgetBase)
        self.stackedWidget.setMinimumSize(QtCore.QSize(350, 300))
        self.stackedWidget.setMaximumSize(QtCore.QSize(350, 350))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setMinimumSize(QtCore.QSize(350, 300))
        self.tableWidget.setMaximumSize(QtCore.QSize(350, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(ValueWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(ValueWidgetBase)

    def retranslateUi(self, ValueWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        ValueWidgetBase.setWindowTitle(_translate("ValueWidgetBase", "Form"))
        self.label_4.setText(_translate("ValueWidgetBase", "Weibullparameter (C)"))
        self.label_3.setText(_translate("ValueWidgetBase", "Weibullparameter (K)"))
        self.label_6.setText(_translate("ValueWidgetBase", "Weibullparameter (W)"))
        self.label_7.setText(_translate("ValueWidgetBase", "Rauhigkeitslayer (z0)"))
        self.cbxActive.setToolTip(_translate("ValueWidgetBase", "(Shift+A) to toggle"))
        self.cbxActive.setText(_translate("ValueWidgetBase", "Start/Stop"))
        self.cbxGraph.setToolTip(_translate("ValueWidgetBase", "(Shift+W) to toggle"))
        self.cbxGraph.setText(_translate("ValueWidgetBase", "Weibull"))
        self.label_5.setText(_translate("ValueWidgetBase", "Standort"))
        self.dataName.setToolTip(_translate("ValueWidgetBase", "Name des Standortes angeben"))
        self.dataName.setText(_translate("ValueWidgetBase", "Standort"))
        self.label_11.setText(_translate("ValueWidgetBase", "Radius (z0)"))
        self.label_2.setText(_translate("ValueWidgetBase", "X"))
        self.label.setText(_translate("ValueWidgetBase", "Y"))
        self.buttonSaveAs.setToolTip(_translate("ValueWidgetBase", "(Shift+S) to Save Graph"))
        self.buttonSaveAs.setText(_translate("ValueWidgetBase", "Grafik Speichern"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ValueWidgetBase", "Layer"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Value"))

