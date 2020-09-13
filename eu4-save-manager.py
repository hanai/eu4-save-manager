from PySide2.QtWidgets import QMainWindow, QDialog, QFileDialog, QApplication, QMessageBox

import sys
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from ui.MainWindow import Ui_MainWindow
from ui.AboutDialog import Ui_AboutDialog


class Watcher():
    def __init__(self):
        self.event_handler = PatternMatchingEventHandler("*", "", True, False)
        self.event_handler.on_created = self.on_created
        self.event_handler.on_modified = self.on_modified

    def on_created(self, event):
        print('created', event.src_path)

    def on_modified(self, event):
        print('modified', event.src_path)

    def change_path(self, path):
        self.path = path

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

    def initCentralWidget(self):
        self.ui.pushButton_selectSaveDir.clicked.connect(
            self.selectSaveDirClick)
        self.ui.pushButton_run.clicked.connect(self.btnRunClick)

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
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
