#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:20:26 2019

@author: fubar

In this tutorial, let us progressively build a PyQt App in which we read
the state value (the slider Position) of a QWidget like Slider
and write the state value to another QWidget like the QTextEdit.

Step 2: Slot one of the LineEdit's signal to the slot of other LineEdit
and vice versa

"""

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout

app = QApplication([])  # instantiate a Qt App
#
# create a QWidget container widget to hold the Slider and TextEdit boxes
#
myWindow = QWidget()
#
# create two lineEdit widgets
#
myLineEdit1 = QLineEdit()
myLineEdit1.setText('Hello, world!')
myLineEdit2 = QLineEdit()
myLineEdit2.setText('Bye, world!')
#
# create the layout
#
layout = QVBoxLayout()          # create the layout
layout.addWidget(myLineEdit1)      # populate the layout with the created widgets
layout.addWidget(myLineEdit2)     # ...
#
# Set the above layout to the above window
#
myWindow.setLayout(layout)                # set the layout for the window
myWindow.show()                           # draw the window
#
# Event handlers
#
def onReturnPressed1():
    textlisten = myLineEdit1.text()
    myLineEdit2.setText(textlisten)
def onReturnPressed2():
    textlisten = myLineEdit2.text()
    myLineEdit1.setText(textlisten)
#
# Signals
#
myLineEdit1.returnPressed.connect(onReturnPressed1)
myLineEdit2.returnPressed.connect(onReturnPressed2)
#
# hand over the control to the Qt App
#
app.exec_()