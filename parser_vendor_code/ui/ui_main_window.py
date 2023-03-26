# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.checkBoxAuto = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAuto.setChecked(True)
        self.checkBoxAuto.setObjectName("checkBoxAuto")
        self.horizontalLayout_2.addWidget(self.checkBoxAuto)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditInput = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput.setInputMask("")
        self.lineEditInput.setObjectName("lineEditInput")
        self.horizontalLayout.addWidget(self.lineEditInput)
        self.pushButtonParse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonParse.setObjectName("pushButtonParse")
        self.horizontalLayout.addWidget(self.pushButtonParse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuet = QtWidgets.QAction(MainWindow)
        self.actionQuet.setObjectName("actionQuet")
        self.actionTemplates = QtWidgets.QAction(MainWindow)
        self.actionTemplates.setObjectName("actionTemplates")
        self.actionDirectories = QtWidgets.QAction(MainWindow)
        self.actionDirectories.setEnabled(True)
        self.actionDirectories.setObjectName("actionDirectories")
        self.actionLocalPath = QtWidgets.QAction(MainWindow)
        self.actionLocalPath.setObjectName("actionLocalPath")
        self.menuFile.addAction(self.actionTemplates)
        self.menuFile.addAction(self.actionDirectories)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLocalPath)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuet)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuet.triggered.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Разбираем артикул"))
        self.checkBoxAuto.setText(
            _translate("MainWindow", "Автоматическое\n" "определение")
        )
        self.lineEditInput.setPlaceholderText(_translate("MainWindow", "..."))
        self.pushButtonParse.setText(_translate("MainWindow", "Разобрать"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ключ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Значение"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.actionQuet.setText(_translate("MainWindow", "Выход"))
        self.actionTemplates.setText(_translate("MainWindow", "Шаблоны"))
        self.actionDirectories.setText(_translate("MainWindow", "Каталоги/Справочники"))
        self.actionLocalPath.setText(_translate("MainWindow", "Локальные настройки"))
