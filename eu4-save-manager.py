from PySide2.QtWidgets import QMainWindow, QDialog, QFileDialog, QApplication

import sys
from pathlib import Path

from ui.MainWindow import Ui_MainWindow
from ui.AboutDialog import Ui_AboutDialog


class AboutDialog(QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accept)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.runState = False
        self.currentSelectedSaveDir = ''

        self.initWindow()

    def initWindow(self):
        self.initMenuBar()
        self.initCentralWidget()

    def selectSaveDirClick(self):
        dir = QFileDialog.getExistingDirectory(self, '选择存档文件目录',
                                               str(Path.home()))
        if (dir != ''):
            self.onSaveFileDirChange(dir)

    def btnRunClick(self):
        if self.runState == True:
            self.ui.pushButton_run.setText('开始')
            self.runState = False
        else:
            if self.currentSelectedSaveDir != '':
                self.ui.pushButton_run.setText('停止')
                self.runState = True

    def initCentralWidget(self):
        self.ui.pushButton_selectSaveDir.clicked.connect(
            self.selectSaveDirClick)
        self.ui.pushButton_run.clicked.connect(self.btnRunClick)

    def onSaveFileDirChange(self, dir):
        self.ui.label_saveDir.setText(dir)
        self.currentSelectedSaveDir = dir

    def initMenuBar(self):
        self.ui.action_exit.triggered.connect(app.exit)
        self.ui.action_about.triggered.connect(
            lambda _: self.showAboutDialog())

    def showAboutDialog(self):
        dlg = AboutDialog()
        dlg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
