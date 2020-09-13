from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
from pathlib import Path

from MainWindow import Ui_MainWindow


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('关于')

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel('欧陆风云4 存档管理器')
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        layout.addWidget(QLabel('版本：0.0.1'))
        layout.addWidget(QLabel('作者：槑小呆'))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


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
