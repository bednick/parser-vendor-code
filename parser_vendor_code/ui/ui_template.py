# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/template.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogUpsertTemplate(object):
    def setupUi(self, DialogUpsertTemplate):
        DialogUpsertTemplate.setObjectName("DialogUpsertTemplate")
        DialogUpsertTemplate.resize(900, 600)
        DialogUpsertTemplate.setMinimumSize(QtCore.QSize(900, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogUpsertTemplate)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelName = QtWidgets.QLabel(DialogUpsertTemplate)
        self.labelName.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(DialogUpsertTemplate)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelValue = QtWidgets.QLabel(DialogUpsertTemplate)
        self.labelValue.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing
        )
        self.labelValue.setObjectName("labelValue")
        self.gridLayout.addWidget(self.labelValue, 3, 0, 1, 1)
        self.textEditValue = QtWidgets.QTextEdit(DialogUpsertTemplate)
        self.textEditValue.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textEditValue.setTabChangesFocus(True)
        self.textEditValue.setHtml(
            '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
            '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>'
        )
        self.textEditValue.setAcceptRichText(False)
        self.textEditValue.setObjectName("textEditValue")
        self.gridLayout.addWidget(self.textEditValue, 3, 1, 1, 1)
        self.lineEditMask = QtWidgets.QLineEdit(DialogUpsertTemplate)
        self.lineEditMask.setObjectName("lineEditMask")
        self.gridLayout.addWidget(self.lineEditMask, 1, 1, 1, 1)
        self.labelMask = QtWidgets.QLabel(DialogUpsertTemplate)
        self.labelMask.setTextFormat(QtCore.Qt.AutoText)
        self.labelMask.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.labelMask.setObjectName("labelMask")
        self.gridLayout.addWidget(self.labelMask, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.listWidgetTemplateItems = QtWidgets.QListWidget(DialogUpsertTemplate)
        self.listWidgetTemplateItems.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.listWidgetTemplateItems.setMovement(QtWidgets.QListView.Static)
        self.listWidgetTemplateItems.setObjectName("listWidgetTemplateItems")
        self.verticalLayout.addWidget(self.listWidgetTemplateItems)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogUpsertTemplate)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save
        )
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(DialogUpsertTemplate)
        self.buttonBox.accepted.connect(DialogUpsertTemplate.accept)  # type: ignore
        self.buttonBox.rejected.connect(DialogUpsertTemplate.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogUpsertTemplate)

    def retranslateUi(self, DialogUpsertTemplate):
        _translate = QtCore.QCoreApplication.translate
        DialogUpsertTemplate.setWindowTitle(
            _translate("DialogUpsertTemplate", "upsert template")
        )
        self.labelName.setText(_translate("DialogUpsertTemplate", "Название:"))
        self.labelValue.setText(_translate("DialogUpsertTemplate", "Шаблон:"))
        self.labelMask.setText(_translate("DialogUpsertTemplate", "Маска:"))
