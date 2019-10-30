#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:38:33 2019

@author: fubar

In this tutorial, let us progressively build a PyQt App in which we read
the state value (the slider Position) of a QWidget like Slider
and write the state value to another QWidget like the QTextEdit.

Step 0: Create a slider object
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QSlider

app = QApplication([])  # instantiate a Qt App
#
# create a Slider widget
#
mySlider = QSlider(Qt.Horizontal)
mySlider.setValue(25)
#
# show the widget
#
mySlider.show()
#
# hand over the control to the Qt App
#
app.exec_()