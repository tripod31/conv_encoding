#!/usr/bin/env python3
# coding:utf-8
'''
Created on 2015/06/16

@author: yoshi
'''
import sys
import io
import os
from mainform import QtGui,Ui_MainWindow    # @UnresolvedImport
from conv_encoding import process           # @UnresolvedImport
from PyQt4.QtCore import QSettings,QObject,SIGNAL
from PyQt4.Qt import QFont

class MyForm(QtGui.QMainWindow):
    '''
    settings file
    '''
    SAVE_FILE=os.path.join(os.path.dirname(__file__), "form_value.txt")
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_encoding.addItem("skip")
        self.ui.comboBox_encoding.addItem("utf-8")
        self.ui.comboBox_encoding.addItem("shift_jis")
        self.ui.comboBox_eol.addItem("skip")
        self.ui.comboBox_eol.addItem("CRLF")
        self.ui.comboBox_eol.addItem("LF")
        self.ui.pushButton_dir.clicked.connect(self.choose_dir)
        self.ui.pushButton_exec.clicked.connect(self.execute)
        self.ui.lineEdit_pattern.setText("*.txt")
        #メニューのコールバック設定
        QObject.connect(self.ui.actionFont, SIGNAL('triggered()'), self.choose_font)
        
        self.load_settings()
        
    '''
    window close event
    '''
    def closeEvent(self, *args, **kwargs):
        self.save_settings()
        return QtGui.QMainWindow.closeEvent(self, *args, **kwargs)
        
    
    def choose_dir(self):
        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        start_dir = self.ui.lineEdit_start_dir.text()
        if os.path.exists(start_dir):
            dialog.setDirectory(start_dir)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            if len(fileNames)>0:
                self.ui.lineEdit_start_dir.setText(fileNames[0])

    def choose_font(self):
        cur_f = self.font()
        f,ok = QtGui.QFontDialog.getFont(cur_f)
        if ok:
            self.setFont(f)
            self.ui.centralwidget.setFont(f)    #コンテナのフォントを変えると全ての子のフォントが変わる
            
    '''
    execute button
    '''    
    def execute(self):
        start_dir = self.ui.lineEdit_start_dir.text()
        pattern = self.ui.lineEdit_pattern.text()
        to_encoding = self.ui.comboBox_encoding.currentText()
        to_eol = self.ui.comboBox_eol.currentText()
        preview = self.ui.checkBox_preview.isChecked()
        
        output = io.StringIO()
        sys.stdout = output
        process(start_dir,pattern,to_encoding,to_eol,preview)
        s= output.getvalue()
        sys.stdout = sys.__stdout__
        self.ui.textEdit_output.setPlainText(s)
    
    def save_settings(self):
        start_dir = self.ui.lineEdit_start_dir.text()
        to_encoding = self.ui.comboBox_encoding.currentIndex()
        to_eol = self.ui.comboBox_eol.currentIndex()
        preview = self.ui.checkBox_preview.isChecked()
        pattern = self.ui.lineEdit_pattern.text()
                
        settings = QSettings(self.SAVE_FILE,
                                  QSettings.IniFormat)
        if settings.Status != QSettings.AccessError:
            settings.beginGroup("form_value")
            settings.setValue("start_dir", start_dir)
            settings.setValue("to_encoding", to_encoding)
            settings.setValue("to_eol", to_eol)
            settings.setValue("preview", preview)
            settings.setValue("pattern", pattern)
            settings.setValue("geometry",self.saveGeometry())
            settings.setValue("font",self.font().toString())    
            settings.endGroup()
    
    def load_settings(self):
        if not os.path.exists(self.SAVE_FILE):
            return
        
        settings = QSettings(self.SAVE_FILE,
                                  QSettings.IniFormat)
        if settings.Status != QSettings.AccessError:
            settings.beginGroup("form_value")
            self.ui.lineEdit_start_dir.setText(settings.value('start_dir'))
            self.ui.comboBox_encoding.setCurrentIndex(settings.value("to_encoding",type=int))
            self.ui.comboBox_eol.setCurrentIndex(settings.value("to_eol",type=int))
            self.ui.checkBox_preview.setChecked(settings.value('preview',type=bool))
            self.ui.lineEdit_pattern.setText(settings.value('pattern'))
            self.restoreGeometry(settings.value("geometry"))
            self.font().fromString(settings.value("font"))
            f=QFont()
            if f.fromString(settings.value("font")):
                self.setFont(f)
            settings.endGroup()
           
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
