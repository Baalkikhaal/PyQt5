#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:38:33 2019

@author: fubar

In this tutorial, let us progressively build a PyQt App in which we read
the state value (the slider Position) of a QWidget like Slider
and write the state value to another QWidget like the QTextEdit.

Step 3: Read the LineEdit value and print to standard output

"""

from PyQt5.QtWidgets import QApplication, QLineEdit

app = QApplication([])  # instantiate a Qt App
#
# create a Slider widget
#
myLineEdit = QLineEdit()
myLineEdit.setText("Hello, world!")
#
# show the widget
#
myLineEdit.show()
#
# Event handler
#
def onReturnPressed():
    '''Print the text to stdout in the lineEdit widget on pressing return'''
    textlisten = myLineEdit.text()
    print(textlisten)
#
# Signal
#
myLineEdit.returnPressed.connect(onReturnPressed)
#
# hand over the control to the Qt App
#
app.exec_()