#!/usr/bin/env python
import sys
import os
from PySide import *
import Model
"""
#OS X 10.9.3
#using PySide 1.2.1
#using Qt 4.8.6
#chmod +x this file, then cd [wherever this is], ./Risk2210.py
"""

gfxOff = 40
width, height = 800, 600


class boardGUI(QtGui.QWidget): #cannot be QtGui.QMainWindow or button layout fails

	def __init__(self):
		super(boardGUI, self).__init__()
		self.initUI()
	
	def buttonSetup(self):
		quitbtn = QtGui.QPushButton('Quit', self)
		buttons = QtGui.QGridLayout()
		buttons.setVerticalSpacing(2)
		buttons.addWidget(quitbtn, 1, 1)
		self.setLayout(buttons)
		quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
	
	def mapUnderlay(self):
		earth = QtGui.QLabel(self)
		earth.setGeometry(0, 0, width, height)
		#use full ABSOLUTE path to the image, not relative
		earth.setPixmap(QtGui.QPixmap(os.getcwd() + "/Background.png"))
		
		
	def initUI(self):
		self.mapUnderlay()
		self.buttonSetup()
		self.setGeometry(gfxOff, gfxOff, width, height)
		self.setWindowTitle('Eight Minute Empire: Legends')
		#self.setWindowIcon(QtGui.QIcon('web.png'))		this for title bar
		self.show()


def main():
	app = QtGui.QApplication(sys.argv)
	ex = boardGUI()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
	
"""
plan for graphics:
qVerticalLayout, three tall
	top is cards to purchase
	middle has horizontal layout, 3 maps
	bottom has horizontal layout, 1 map in the middle, info on the sides
popup will ask relevant setup information, or in the beginning it will be passed in through the terminal
"""

#http://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python