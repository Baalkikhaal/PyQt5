from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QWidget, QSlider, QLineEdit, QVBoxLayout

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
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
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
