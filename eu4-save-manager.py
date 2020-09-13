from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
from pathlib import Path

from ui.MainWindow import Ui_MainWindow
from ui.AboutDialog import Ui_AboutDialog


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.accept)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.initWindow()

    def initWindow(self):
        self.initMenuBar()
        self.pushButton_selectSaveDir.clicked.connect(self.selectSaveDirClick)

    def selectSaveDirClick(self):
        dir = QFileDialog.getExistingDirectory(self, '选择存档文件目录',
                                               str(Path.home()))
        if (dir != ''):
            self.onSaveFileDirChange(dir)

    def onSaveFileDirChange(self, dir):
        self.label_saveDir.setText(dir)
        self.currentSelectedSaveFileDir = dir

    def initMenuBar(self):
        self.action_exit.triggered.connect(qApp.quit)
        self.action_about.triggered.connect(lambda _: self.showAboutDialog())

    def showAboutDialog(self):
        dlg = AboutDialog()
        dlg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
