#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:07:25 2019

@author: fubar

In this tutorial, let us progressively build a PyQt App in which we read
the state value (the slider Position) of a QWidget like Slider
and write the state value to another QWidget like the QTextEdit.

Step 1: I do not know how to get the state value of the slider.
Instead let me try it with QLineEdit. So create a pair of LineEdit in a 
Vertical Box Layout

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
# hand over the control to the Qt App
#
app.exec_()