#!/bin/bash
PYTHONOPTIMIZE=2 pyinstaller -y -w --clean --log-level=WARN -n EU4SaveManager -F --exclude-module email --exclude-module urllib.request --exclude-module unittest --exclude-module pdb --exclude-module PySide2.QtNetwork eu4-save-manager.py
