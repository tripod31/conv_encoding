# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(875, 535)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_start_dir = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_start_dir.setObjectName(_fromUtf8("lineEdit_start_dir"))
        self.horizontalLayout.addWidget(self.lineEdit_start_dir)
        self.pushButton_dir = QtGui.QPushButton(self.centralwidget)
        self.pushButton_dir.setObjectName(_fromUtf8("pushButton_dir"))
        self.horizontalLayout.addWidget(self.pushButton_dir)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_pattern = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_pattern.setText(_fromUtf8(""))
        self.lineEdit_pattern.setObjectName(_fromUtf8("lineEdit_pattern"))
        self.gridLayout_2.addWidget(self.lineEdit_pattern, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_encoding = QtGui.QComboBox(self.centralwidget)
        self.comboBox_encoding.setObjectName(_fromUtf8("comboBox_encoding"))
        self.gridLayout_2.addWidget(self.comboBox_encoding, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_eol = QtGui.QComboBox(self.centralwidget)
        self.comboBox_eol.setObjectName(_fromUtf8("comboBox_eol"))
        self.gridLayout_2.addWidget(self.comboBox_eol, 3, 1, 1, 1)
        self.textEdit_output = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_output.setObjectName(_fromUtf8("textEdit_output"))
        self.gridLayout_2.addWidget(self.textEdit_output, 4, 1, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_preview = QtGui.QPushButton(self.widget)
        self.pushButton_preview.setObjectName(_fromUtf8("pushButton_preview"))
        self.gridLayout.addWidget(self.pushButton_preview, 0, 0, 1, 1)
        self.pushButton_exec = QtGui.QPushButton(self.widget)
        self.pushButton_exec.setObjectName(_fromUtf8("pushButton_exec"))
        self.gridLayout.addWidget(self.pushButton_exec, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFont = QtGui.QAction(MainWindow)
        self.actionFont.setObjectName(_fromUtf8("actionFont"))
        self.actionLanguage = QtGui.QAction(MainWindow)
        self.actionLanguage.setObjectName(_fromUtf8("actionLanguage"))
        self.menuView.addAction(self.actionFont)
        self.menuView.addAction(self.actionLanguage)
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "conv_encoding", None))
        self.label.setText(_translate("MainWindow", "start directory", None))
        self.pushButton_dir.setText(_translate("MainWindow", "...", None))
        self.label_3.setToolTip(_translate("MainWindow", "wild card format", None))
        self.label_3.setText(_translate("MainWindow", "file name pattern", None))
        self.label_2.setText(_translate("MainWindow", "encoding", None))
        self.label_4.setText(_translate("MainWindow", "end of line", None))
        self.pushButton_preview.setText(_translate("MainWindow", "preview", None))
        self.pushButton_exec.setText(_translate("MainWindow", "execute", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionFont.setText(_translate("MainWindow", "Font", None))
        self.actionLanguage.setText(_translate("MainWindow", "Language", None))

