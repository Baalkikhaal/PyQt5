#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:38:00 2019

@author: fubar

This script demonstrates the layout features of PyQt.
Case under study is the  QVBoxLayout()

Reference : https://build-system.fman.io/pyqt5-tutorial
"""

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#
# Create the Application instance. This is a requirement.
#
app = QApplication([])
#
# Create the widgets required for the app
#
window = QWidget()      # create a window of type QWidget
topButton       = QPushButton('Top')    # create push button Top
bottomButton    = QPushButton('Bottom') # create push button Bottom
#
# Create the layout of the widgets using QVBoxLayout
#
layout = QVBoxLayout()                  # create the layout
layout.addWidget(QPushButton('Top'))    # populate the layout with the created widgets
layout.addWidget(QPushButton('Bottom')) # ...
#
# Set the above layout to the above window
#
window.setLayout(layout)                # set the layout for the window
window.show()                           # draw the window
app.exec_()                             # give control of the window to Qt till the user closes it!