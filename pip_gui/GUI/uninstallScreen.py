# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uninstallScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(428, 457)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 261, 381))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 60, 121, 98))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnUninstall = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnUninstall.setObjectName(_fromUtf8("btnUninstall"))
        self.verticalLayout.addWidget(self.btnUninstall)
        self.btnUninstallAll = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnUninstallAll.setObjectName(_fromUtf8("btnUninstallAll"))
        self.verticalLayout.addWidget(self.btnUninstallAll)
        self.btnBack = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnBack.setObjectName(_fromUtf8("btnBack"))
        self.verticalLayout.addWidget(self.btnBack)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Uninstall Packages", None))
        self.label.setText(_translate("Form", "Please select the packages you want to uninstall:", None))
        self.btnUninstall.setText(_translate("Form", "Uninstall", None))
        self.btnUninstallAll.setText(_translate("Form", "Uninstall All", None))
        self.btnBack.setText(_translate("Form", "Go Back", None))

