#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:25:00 2019

@author: fubar
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
	"""Class definition for the Window application called ListKeeper that lets us view, add, edit text as a list and lets us save the lists to the hard drive.

It is a derived class inheriting attributes and methods froms its parent QMainWindow class."""
	def __init__(self, parent=None):
		"""Initialize method to instantiate MainWindow class object"""
		super(MainWindow, self).__init__(parent) # what is super?
		self.filename 	= None
		self.dirty 	= False
		self.listWidget	= QListWidget()			# set listWidget attribute to listWidget
		self.setCentralWidget(self.listWidget)	# set central widget of the window/form to listWidget
		#
		# Set the File handling actions. Every action is defined as QAction object. This object holds a menu text, a method to be called when the object is invoked, a keyboard shortcut, and an icon.
		#
		fileNewAction 	= self.createAction("&New...", self.fileNew, QKeySequence.New, "filenew")
		fileOpenAction 	= self.createAction("&Open...", self.fileOpen, QKeySequence.Open, "fileopen")
		fileSaveAction	= self.createAction("&Save...", self.fileSave, QKeySequence.Save, "filesave")
		#
		# create a menu widget and add the above defined actions to the menu
		#
		fileMenu = self.menuBar().addMenu("&File")	#create a menu Widget
		fileMenu.addAction(fileNewAction)		# add NewFile Action to the menu
		fileMenu.addAction(fileOpenAction)		# ...
		fileMenu.addAction(fileSaveAction)		# ...
		#
		# create a toolbar widget and add the same actions to it
		#
		fileToolbar 	= self.addToolBar("File")	# create a Toolbar Widget
		fileToolbar.addAction(fileNewAction)	# add NewFile Action to the toolbar
		fileToolbar.addAction(fileOpenAction)	# ...
		fileToolbar.addAction(fileSaveAction)	# ...
		#
		# Add a timed out Status message for the Status bar. Also add a Window title
		#
		self.statusBar().showMessage("Ready...", 5000)
		self.setWindowTitle("ListKeeper - Unnamed List")

if __name__ == '__main__':
    app = QApplication([])
    listKeeper = MainWindow()
    listKeeper.show()
    app.exec_()
