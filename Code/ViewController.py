#!/usr/bin/env python
import sys
import os
from PySide import *
import Model
import Cards
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


cards = []

def get_image_directory():
	folder = os.getcwd()
	folders = folder.split("/")
	topics_folder = "/".join(folders[0:folders.index("Topics in CS")+1])
	image_folder = topics_folder + "/Image Resources/"
	return image_folder
	
	

def populate_cards():
	for c in Cards.get_cards():
		cards.append(Model.card(c[0],c[1],c[2],c[3],c[4],c[5]))


class boardGUI(QtGui.QWidget): #cannot be QtGui.QMainWindow or button layout fails
	
	def __init__(self):
		super(boardGUI, self).__init__()
		self.initModel()
		self.initUI()
	
	def layoutSetup(self):
		imageDirectory = get_image_directory()
		cards_directory = imageDirectory + "/Cards/"
		maps_directory = imageDirectory + "/Maps/"
	
		vertical = QtGui.QVBoxLayout()
		
		
		cardsRowOne = QtGui.QHBoxLayout()
		
		UIcards = []
		
		for i in range(6):
			card = QtGui.QLabel(self)
			UIcards.append(card)
			image_name = "".join(cards[i].name.split(" "))
			UIcards[-1].setPixmap(QtGui.QPixmap(cards_directory + "%s.jpeg" % image_name))
			cardsRowOne.addWidget(UIcards[-1])
			
			
			
		mapRowTwo = QtGui.QHBoxLayout()
		
		maps = []
		
		for i in range(4):
			map = QtGui.QLabel(self)
			maps.append(map)
			maps[-1].setPixmap(QtGui.QPixmap(maps_directory + "map%s-A.png" % str(i)))
		
		
		
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
		
		
	def initModel(self):
		populate_cards()
		
		
		
		
	def initUI(self):
		self.layoutSetup()
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
