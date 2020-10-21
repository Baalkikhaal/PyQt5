#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:31:14 2019

@author: fubar

Tutorial on OpenCV

**Canny Edge Detection**

Reference:

[Canny Edge Detection using OpenCV](https://opencv-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html)

[Embedding Matplotlib in Qt](https://matplotlib.org/gallery/user_interfaces/embedding_in_qt_sgskip.html#sphx-glr-gallery-user-interfaces-embedding-in-qt-sgskip-py)

Exercise:
    Write a small application to find the Canny edge detection

    whose threshold values can be varied using two trackbars. 

    This way, you can understand the effect of threshold values.

Solution:
    Let us use PyQt for the GUI application.
    
    Need SlideBar Widget
    
    Image Holding Widget: For this use Matplotlib's Qt5 backend
    
Design:
|---------------------------------------------------|
|               Canny Edge App                      |
|---------------------------------------------------|
|                                                   |
|   ----------- ----     -----------------------    |
|  | QLineEdit | OK |   |                       |   |  
|   ----------------    |       Input           |   |
|                       |       Image           |   |
|   ----------------    |                       |   |
|  | ======#======= |    -----------------------    |
|   ----------------                                |
|   QSlider: L Thres     -----------------------    |
|                       |                       |   |
|   ----------------    |       Canny           |   |
|  | ===========#== |   |       Image           |   |
|   ----------------    |                       |   |
|   QSlider: U Thres     -----------------------    |
|---------------------------------------------------|
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLineEdit, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from matplotlib.backends.qt_compat import is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


import cv2

import os, os.path

app = QApplication([])    # instantiate a PyQt App

# create a Widget to hold all the upcoming subwidgets

myWindow = QWidget()
myWindow.setWindowTitle("Canny Edge Tutorial")

### create the layout.

###     Design is two horizontal layout widgets.

###     The left one hosts the inputs.

###     The right one hosts the outpus.

layout  = QHBoxLayout()

### create the input V layout

#   is a Vertical Layout widget and hosts:

#       QLineEdit to read the filepath of image

#       QSliders for lower and upper thresholds

input_layout = QVBoxLayout()

### create the input widgets

###     LineEdit for reading image filepath
read_filepath   = QLineEdit()
read_filepath.setText(os.path.abspath(os.path.join(os.curdir,'images','wololo.jpg')))
#read_filepath.setText('/home/fubar/Documents/GITprojects/MyGitProjects/CannyEdgeDetection/images/wololo.jpg')

filepathLabel = QLabel("Image filepath:\nPress Enter to read")
filepathLabel.setBuddy(read_filepath)

###     Sliders for Canny thresholds

threshold_lower = QSlider(Qt.Horizontal)
threshold_lower.setMinimum(0)
threshold_lower.setMaximum(255)
threshold_lower.setValue(100)   # default lower threshold
lowerlabel = QLabel("Canny Lower Threshold:\n[0-255]")
lowerlabel.setBuddy(threshold_lower)

threshold_upper = QSlider(Qt.Horizontal)
threshold_upper.setMinimum(0)
threshold_upper.setMaximum(255)
threshold_upper.setValue(200)   # default upper threshold
upperlabel = QLabel("Canny Upper Threshold:\n[0-255]")
upperlabel.setBuddy(threshold_upper)

### add the widgets to the input layout

input_layout.addWidget(filepathLabel)
input_layout.addWidget(read_filepath)
input_layout.addWidget(lowerlabel)
input_layout.addWidget(threshold_lower)
input_layout.addWidget(upperlabel)
input_layout.addWidget(threshold_upper)

### create the output V layout

###     is a Vertical layout widget and hosts:

###     FigureCanvas() for holding matplotlib Image

output_layout = QVBoxLayout()

### create the output widgets

static_canvas   = FigureCanvas(Figure(figsize=(5, 5)))
static_ax       = static_canvas.figure.subplots()
# we will draw the canvas later; after defining the drawing functions

dynamic_canvas  = FigureCanvas(Figure(figsize=(5, 5)))
dynamic_ax      = dynamic_canvas.figure.subplots()
# we will draw the canvas later; after defining the drawing functions


### add the widgets to the output layout

output_layout.addWidget(static_canvas)
output_layout.addWidget(dynamic_canvas)
# add the input and output layouts to the main layout

layout.addLayout(input_layout)
layout.addLayout(output_layout)

# now that the layout is created, set the layout to the main window widget

myWindow.setLayout(layout)


# event handlers here

def updateStaticCanvas():
    ''' Once the Line Edit is returned, read the image and
        draw on the FigureCanvas()'''
    # read the image from filepath given in lineedit
    img_filepath    = read_filepath.text()
    img_static             = cv2.imread(img_filepath, cv2.IMREAD_GRAYSCALE)
    
    # clear the current image
    static_ax.clear()
    
    # buffer the update image
    static_ax.imshow(img_static)
    
    # draw the image on the Qt backend FigureCanvas
    static_ax.figure.canvas.draw()
    
def updateDynamicCanvas():
    #read the updated lower and upper thresholds
    lower = threshold_lower.sliderPosition()
    print(f"the lower threshold is {lower}")
    upper = threshold_upper.sliderPosition()
    print(f"the upper threshold is {upper}")

    # read the image from filepath given in lineedit
    img_filepath    = read_filepath.text()
    
    # clear the current image
    dynamic_ax.clear()
    
    # update the image
    
    img_dynamic = cv2.imread(img_filepath, cv2.IMREAD_GRAYSCALE)
    img_med     = cv2.medianBlur(img_dynamic, 5)
    img_canny   = cv2.Canny(img_med, lower, upper)
#    x = np.linspace(0, 10, 501)
#    dynamic_ax.plot(x, np.sin(x ** lower))
    
    # buffer the updated image
    dynamic_ax.imshow(img_canny, cmap = 'Greys')
    
    # draw the image on the Qt backend for matplotlib i.e. FigureCanvas
    
    dynamic_ax.figure.canvas.draw()

#    
# signals
#
read_filepath.returnPressed.connect(updateStaticCanvas)
threshold_lower.sliderReleased.connect(updateDynamicCanvas)
threshold_upper.sliderReleased.connect(updateDynamicCanvas)
#
# show the app
#
updateStaticCanvas()
updateDynamicCanvas()

myWindow.show()
#
# hand over the control to the Qt App
#
app.exec_()







