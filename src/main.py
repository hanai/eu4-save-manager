from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QDialog, QFileDialog, QApplication, QMessageBox

import sys
import os
from platform import system
from pathlib import Path
from shutil import copy2
from datetime import datetime
from subprocess import Popen

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from ui.MainWindow import Ui_MainWindow
from ui.AboutDialog import Ui_AboutDialog


class Watcher():
    def __init__(self):
        self.event_handler = PatternMatchingEventHandler(["*.eu4"], "", True,
                                                         False)
        self.event_handler.on_modified = self.on_modified

    def on_modified(self, event):
        if event.src_path.startswith(
                self.bakPath) or 'Backup' in event.src_path:
            return
        file_path = Path(event.src_path)
        new_file_path = os.path.join(
            self.bakPath, file_path.stem +
            datetime.now().strftime('_%y%m%d_%H%M%S') + file_path.suffix)
        copy2(file_path, new_file_path)

    def change_path(self, path):
        self.path = path
        self.mkBakDir()

    def mkBakDir(self):
        bakPath = os.path.join(self.path, 'bak')
        if not os.path.exists(bakPath):
            os.mkdir(bakPath)
        self.bakPath = bakPath

    def start(self):
        self.observer = Observer()
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()


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

        self.watcher = Watcher()

        self.runState = False
        self.currentSelectedSaveDir = ''

        self.initWindow()

    def initWindow(self):
        self.initMenuBar()
        self.initCentralWidget()

    def selectSaveDirClick(self):
        dir = QFileDialog.getExistingDirectory(
            self, '选择存档文件目录', self.currentSelectedSaveDir
            if self.currentSelectedSaveDir != '' else str(Path.home()))
        if (dir != ''):
            self.onSaveDirChange(dir)

    def btnRunClick(self):
        if self.runState:
            self.ui.pushButton_run.setText('开始')
            self.ui.pushButton_selectSaveDir.setDisabled(False)
            self.watcher.stop()
            self.runState = False
        else:
            if self.currentSelectedSaveDir != '':
                self.ui.pushButton_selectSaveDir.setDisabled(True)
                self.ui.pushButton_run.setText('停止')
                self.watcher.start()
                self.runState = True
            else:
                QMessageBox.warning(self, "提示", "请先选择存档文件所在目录")

    def btnOpenSaveFolderClick(self):
        folder_path = self.currentSelectedSaveDir
        if folder_path != '':
            plt = system()
            if (plt == 'Linux'):
                Popen(['xdg-open', folder_path])
            elif (plt == 'Windows'):
                os.startfile(folder_path)
            elif (plt == 'Darwin'):
                os.system('open "%s"' % folder_path)

    def initCentralWidget(self):
        self.ui.pushButton_selectSaveDir.clicked.connect(
            self.selectSaveDirClick)
        self.ui.pushButton_run.clicked.connect(self.btnRunClick)
        self.ui.pushButton_openFolder.clicked.connect(
            self.btnOpenSaveFolderClick)

    def onSaveDirChange(self, path):
        self.ui.label_saveDir.setText(path)
        self.currentSelectedSaveDir = path
        self.watcher.change_path(path)

    def initMenuBar(self):
        self.ui.action_exit.triggered.connect(app.exit)
        self.ui.action_about.triggered.connect(
            lambda _: self.showAboutDialog())

    def showAboutDialog(self):
        dlg = AboutDialog()
        dlg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
