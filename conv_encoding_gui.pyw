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
from PyQt4.QtCore import QSettings

class MyForm(QtGui.QMainWindow):
    '''
    設定ファイル
    スクリプトと同じディレクトリに置く
    '''
    SAVE_FILE=os.path.join(os.path.dirname(__file__), "form_value.txt")
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_encoding.addItem("utf-8")
        self.ui.comboBox_encoding.addItem("cp932")
        self.ui.pushButton_dir.clicked.connect(self.choose_dir)
        self.ui.pushButton_exec.clicked.connect(self.execute)
        self.ui.lineEdit_pattern.setText("*.txt")
        self.load_settings()
        
    '''
    window close時
    '''
    def closeEvent(self, *args, **kwargs):
        self.save_settings()
        return QtGui.QMainWindow.closeEvent(self, *args, **kwargs)
        
    
    def choose_dir(self):
        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            if len(fileNames)>0:
                self.ui.lineEdit_start_dir.setText(fileNames[0])

    '''
    実行ボタン
    '''    
    def execute(self):
        start_dir = self.ui.lineEdit_start_dir.text()
        to_encoding = self.ui.comboBox_encoding.currentText()
        preview = self.ui.checkBox_preview.isChecked()
        pattern = self.ui.lineEdit_pattern.text()
        
        output = io.StringIO()
        sys.stdout = output
        process(start_dir,to_encoding,preview,pattern)
        s= output.getvalue()
        sys.stdout = sys.__stdout__
        self.ui.textEdit_output.setPlainText(s)
    
    def save_settings(self):
        start_dir = self.ui.lineEdit_start_dir.text()
        to_encoding = self.ui.comboBox_encoding.currentIndex()
        preview = self.ui.checkBox_preview.isChecked()
        pattern = self.ui.lineEdit_pattern.text()
                
        settings = QSettings(self.SAVE_FILE,
                                  QSettings.IniFormat)
        if settings.Status != QSettings.AccessError:
            settings.beginGroup("form_value")
            settings.setValue("start_dir", start_dir)
            settings.setValue("to_encoding", to_encoding)
            settings.setValue("preview", preview)
            settings.setValue("pattern", pattern)
            settings.setValue("geometry",self.saveGeometry())    
            settings.endGroup()
    
    def load_settings(self):
        settings = QSettings(self.SAVE_FILE,
                                  QSettings.IniFormat)
        if settings.Status != QSettings.AccessError:
            settings.beginGroup("form_value")
            self.ui.lineEdit_start_dir.setText(settings.value('start_dir'))
            self.ui.comboBox_encoding.setCurrentIndex(settings.value("to_encoding",type=int))
            self.ui.checkBox_preview.setChecked(settings.value('preview',type=bool))
            self.ui.lineEdit_pattern.setText(settings.value('pattern'))
            self.restoreGeometry(settings.value("geometry"));
            settings.endGroup()
           
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())