#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:49:23 2019

@author: fubar

This scripts demonstrates the styling features of PyQt.
Case under study is setting the global app style, QPallette.

Reference : https://build-system.fman.io/pyqt5-tutorial

"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton

#
# Set the global style using setStyle() method
#
app = QApplication([])
app.setStyle('Fusion')
#
# use QPallete to deal with colors and apply changes globally to app's setPallete()
#
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
#
# Widgets creation
#
button = QPushButton('Hello World')
#
# Widget drawing
#
button.show()
#
# Widget control to Qt
#
app.exec_()