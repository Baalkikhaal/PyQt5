#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:31:30 2019

@author: fubar

Hello world PyQt-Gui program

Reference : https://build-system.fman.io/pyqt5-tutorial

"""

from PyQt5.QtWidgets import QApplication, QLabel
app = QApplication([])          # instantiate a PyQt App. This is a requirement
label = QLabel('Hello World!')  # create a label widget
label.show()                    # show the widtget
app.exec_()                     # hand over the control to the app
