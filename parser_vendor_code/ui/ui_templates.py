# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/templates.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogTemplates(object):
    def setupUi(self, DialogTemplates):
        DialogTemplates.setObjectName("DialogTemplates")
        DialogTemplates.resize(1254, 459)
        DialogTemplates.setBaseSize(QtCore.QSize(1200, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogTemplates)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableViewTemplates = QtWidgets.QTableView(DialogTemplates)
        self.tableViewTemplates.setMinimumSize(QtCore.QSize(1200, 400))
        self.tableViewTemplates.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )
        self.tableViewTemplates.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.tableViewTemplates.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows
        )
        self.tableViewTemplates.setObjectName("tableViewTemplates")
        self.tableViewTemplates.horizontalHeader().setDefaultSectionSize(300)
        self.tableViewTemplates.horizontalHeader().setStretchLastSection(True)
        self.tableViewTemplates.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableViewTemplates)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonNew = QtWidgets.QPushButton(DialogTemplates)
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.horizontalLayout.addWidget(self.pushButtonNew)
        self.pushButtonDelete = QtWidgets.QPushButton(DialogTemplates)
        self.pushButtonDelete.setEnabled(False)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogTemplates)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogTemplates)
        self.buttonBox.accepted.connect(DialogTemplates.accept)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogTemplates)

    def retranslateUi(self, DialogTemplates):
        _translate = QtCore.QCoreApplication.translate
        DialogTemplates.setWindowTitle(_translate("DialogTemplates", "Templates"))
        self.pushButtonNew.setText(_translate("DialogTemplates", "NEW"))
        self.pushButtonDelete.setText(_translate("DialogTemplates", "DELETE"))
