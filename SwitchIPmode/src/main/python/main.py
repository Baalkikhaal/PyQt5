#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:08:16 2020

@author: fubar

Qt app to execute Python scripts corresponding to static and dynamic IP

to gain more signal from WiFi hotspots.

iiscwlan hotspot has weak signal at my sitting room location.

As an alternative I use router to generate a local hotspot.

However the downside is the router is configured

to handle only static IP addresses. 

Design:
|---------------------------------------------------|
|              Set IP mode App                      |
|---------------------------------------------------|
|                                                   |
|   ------------------     ---------------------    |
|  | Static IP button |   | Dynamic IP button   |   |  
|   ------------------     ---------------------    |
|---------------------------------------------------|
"""


from fbs_runtime.application_context.PyQt5 import ApplicationContext

import subprocess
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel

import sys


appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

# app = QApplication([])  # instantiate a Qt App
#
# create a QWidget container widget to hold the Buttons for executing scripts
#
window = QWidget()
window.setWindowTitle("Set the mode of IP addressing")

### create the layout.

###     Design is two horizontal layout widgets.

###     The left one hosts the inputs.

###     The right one hosts the events.

layout  = QHBoxLayout()

### create the input V layout

input_layout = QVBoxLayout()

### create the input widgets

###     LineEdit for reading Static IP setscript filepath
read_static_script_filepath   = QLineEdit()

static_script_filepath = r"C:\Users\fubar\Scripts\setStaticIP.py"
read_static_script_filepath.setText(static_script_filepath)
static_script_filepath_Label = QLabel("Static Script filepath:\nPress Enter to read")
static_script_filepath_Label.setBuddy(read_static_script_filepath)

###     LineEdit for reading Static IP setscript filepath
read_dynamic_script_filepath   = QLineEdit()
dynamic_script_filepath = r"C:\Users\fubar\Scripts\setDynamicIP.py"
read_dynamic_script_filepath.setText(dynamic_script_filepath)
dynamic_script_filepath_Label = QLabel("Dynamic Script filepath:\nPress Enter to read")
dynamic_script_filepath_Label.setBuddy(read_dynamic_script_filepath)

### add the widgets to the input layout

input_layout.addWidget(static_script_filepath_Label)
input_layout.addWidget(read_static_script_filepath)
input_layout.addWidget(dynamic_script_filepath_Label)
input_layout.addWidget(read_dynamic_script_filepath)

### create the event V layout

event_layout = QVBoxLayout()

# add button widgets

staticButton       = QPushButton('Set Static IP')    # create push button static
dynamicButton    = QPushButton('Set Dynamic IP') # create push button dynamic

### add the widgets to the event layout

event_layout.addWidget(staticButton)      # populate the layout with the created widgets
event_layout.addWidget(dynamicButton)     # ...

# add the input and event layouts to the main layout

layout.addLayout(input_layout)
layout.addLayout(event_layout)

#
# Event handlers
#

# input event handlers

def updateStaticScriptFilePath():
    global static_script_filepath
    static_script_filepath = read_static_script_filepath.text()

def updateDynamicScriptFilePath():
    global dynamic_script_filepath
    dynamic_script_filepath = read_dynamic_script_filepath.text()

def onStaticButtonClicked():
    global static_script_filepath
    list_command = ['python', static_script_filepath]
#    command = '''python helloWorld.py'''
#    list_command = command.split()
    subprocess.run(list_command)
    
def onDynamicButtonClicked():
    global dynamic_script_filepath
    list_command = ['python', dynamic_script_filepath]
#    command = '''python byeWorld.py'''
#    list_command = command.split()
    subprocess.run(list_command)
#
# Signals
#

# input signals    
read_static_script_filepath.returnPressed.connect(updateStaticScriptFilePath)
read_dynamic_script_filepath.returnPressed.connect(updateDynamicScriptFilePath)

# event_signals    
staticButton.clicked.connect(onStaticButtonClicked)
dynamicButton.clicked.connect(onDynamicButtonClicked)
#

#
# Set the above layout to the above window
#
window.setLayout(layout)                # set the layout for the window
window.show()                           # draw the window

# hand over the control to the Qt App
#

exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
sys.exit(exit_code)