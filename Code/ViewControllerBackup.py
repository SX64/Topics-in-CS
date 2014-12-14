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
width, height = 1300, 600



def otherButton():
	print "this is another button"



class boardGUI(QtGui.QWidget): #cannot be QtGui.QMainWindow or button layout fails

	def __init__(self):
		super(boardGUI, self).__init__()
		self.initUI()
	
	def layoutSetup(self):
		imageDirectory = os.getcwd() + "/Images/"	
	
		vertical = QtGui.QVBoxLayout()
		
		
		cardsRowOne = QtGui.QHBoxLayout()
		
		cards = []
		
		for i in range(6):
			card = QtGui.QLabel(self)
			cards.append(card)
			cards[-1].setFixedWidth(200)
			cards[-1].setFixedHeight(100)
			cards[-1].setPixmap(QtGui.QPixmap(imageDirectory + "card%s.jpeg" % str(i)))
			cardsRowOne.addWidget(cards[-1])
			
			
			
		mapRowTwo = QtGui.QHBoxLayout()
		
		maps = []
		
		for i in range(4):
			map = QtGui.QLabel(self)
			maps.append(map)
			maps[-1].setFixedWidth(400)
			maps[-1].setFixedHeight(200)
			maps[-1].setPixmap(QtGui.QPixmap(imageDirectory + "/map%s.png" % str(i)))
		
		
		
		for i in range(3):
			mapRowTwo.addWidget(maps[i])
		
		
		
		infoRowThree = QtGui.QHBoxLayout()
		
		subVone = QtGui.QVBoxLayout()
		
		otherbtn = QtGui.QPushButton('other', self)
		otherbtn.clicked.connect(otherButton)
		
		
		textArea = QtGui.QLabel(self)
		textArea.setText("example text for whatever")
		
		subVone.addWidget(otherbtn)
		subVone.addWidget(textArea)
		
		quitbtn = QtGui.QPushButton('Quit', self)
		quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		
		infoRowThree.addLayout(subVone)
		infoRowThree.addWidget(maps[-1])
		infoRowThree.addWidget(quitbtn)
		
		
		
		vertical.addLayout(cardsRowOne)
		vertical.addLayout(mapRowTwo)
		vertical.addLayout(infoRowThree)
		self.setLayout(vertical)
		
		
	def initUI(self):
		self.layoutSetup()
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


notes for future:
QScrollArea for main window
look into QLabel more
"""

#http://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python