#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:56:47 2019

@author: fubar

In this tutorial, let us progressively build a PyQt App in which we read
the state value (the slider Position) of a QWidget like Slider
and write the state value to another QWidget like the QTextEdit.

Step 4: Finally 
Create the Slider and LineEdit widgets.
Read the slider value and writer to the line Edit widget.

"""

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLineEdit, QVBoxLayout

app = QApplication([])  # instantiate a Qt App
#
# create a QWidget container widget to hold the Slider and TextEdit boxes
#
myWindow = QWidget()
#
# create a Slider widget
#
mySlider = QSlider()
mySlider.setValue(25)
#
# create a lineEdit widget
myLineEdit = QLineEdit()
myLineEdit.setText('Hello, world!')
#
# create the layout
#
layout = QVBoxLayout()          # create the layout
layout.addWidget(mySlider)      # populate the layout with the created widgets
layout.addWidget(myLineEdit)     # ...
#
# Set the above layout to the above window
#
myWindow.setLayout(layout)                # set the layout for the window
myWindow.show()                           # draw the window
#
# Event handlers
#
def onSliderReleased():
    positionListen = mySlider.sliderPosition()
    myLineEdit.setText(str(positionListen))
#
# Signal
#
mySlider.sliderReleased.connect(onSliderReleased)
#
# hand over the control to the Qt App
#
app.exec_()