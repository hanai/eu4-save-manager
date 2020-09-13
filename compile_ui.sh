#!/bin/bash
python3 -m PyQt5.uic.pyuic ./ui/mainwindow.ui -o ./ui/MainWindow.py
python3 -m PyQt5.uic.pyuic ./ui/aboutdialog.ui -o ./ui/AboutDialog.py