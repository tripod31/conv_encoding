# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\devel_open\eclipse\tools_python\src\conv_encoding\mainform.ui'
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
        MainWindow.resize(752, 482)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_start_dir = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_start_dir.setObjectName(_fromUtf8("lineEdit_start_dir"))
        self.horizontalLayout.addWidget(self.lineEdit_start_dir)
        self.pushButton_dir = QtGui.QPushButton(self.centralwidget)
        self.pushButton_dir.setObjectName(_fromUtf8("pushButton_dir"))
        self.horizontalLayout.addWidget(self.pushButton_dir)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_pattern = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_pattern.setText(_fromUtf8(""))
        self.lineEdit_pattern.setObjectName(_fromUtf8("lineEdit_pattern"))
        self.gridLayout.addWidget(self.lineEdit_pattern, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_encoding = QtGui.QComboBox(self.centralwidget)
        self.comboBox_encoding.setObjectName(_fromUtf8("comboBox_encoding"))
        self.gridLayout.addWidget(self.comboBox_encoding, 2, 1, 1, 1)
        self.pushButton_exec = QtGui.QPushButton(self.centralwidget)
        self.pushButton_exec.setObjectName(_fromUtf8("pushButton_exec"))
        self.gridLayout.addWidget(self.pushButton_exec, 3, 0, 1, 1)
        self.checkBox_preview = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_preview.setObjectName(_fromUtf8("checkBox_preview"))
        self.gridLayout.addWidget(self.checkBox_preview, 3, 1, 1, 1)
        self.textEdit_output = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_output.setObjectName(_fromUtf8("textEdit_output"))
        self.gridLayout.addWidget(self.textEdit_output, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "conv_encoding", None))
        self.label.setText(_translate("MainWindow", "開始ディレクトリ", None))
        self.pushButton_dir.setText(_translate("MainWindow", "…", None))
        self.label_3.setToolTip(_translate("MainWindow", "ワイルドカード形式で設定", None))
        self.label_3.setText(_translate("MainWindow", "変更ファイルパターン", None))
        self.label_2.setText(_translate("MainWindow", "変更先エンコーディング", None))
        self.pushButton_exec.setText(_translate("MainWindow", "実行", None))
        self.checkBox_preview.setText(_translate("MainWindow", "プレビュー", None))
