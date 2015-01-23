#!/usr/bin/env python
import sys
import os
import random
from PySide import *
import Model
import Cards
"""
#OS X 10.9
#using PySide 1.2.1
#using Qt 4.8.6
#chmod +x this file, then cd [wherever this is], ./Risk2210.py
"""


players = []

current_player = 0

def get_current_player():
	return players[current_player]

def change_player():
	global current_player
	old_player = get_current_player()
	old_player.clear()
	print old_player
	b = current_player + 1
	current_player = b if b < len(players) else 0

def populate_players():
	for i in range(4):
		players.append(Model.player(i, 9))

def print_current_player():
	print players[current_player].turn_print()


cards = []

def get_image_directory():
	folder = os.getcwd()
	folders = folder.split("/")
	topics_folder = "/".join(folders[0:-2])
	image_folder = topics_folder + "/Image Resources/"
	return image_folder
	
	

def populate_cards():
	for c in Cards.get_cards():
		cards.append(Model.card(c[0],c[1],c[2],c[3],c[4],c[5]))
		random.shuffle(cards)




class boardGUI(QtGui.QWidget): #cannot be QtGui.QMainWindow or button layout fails
	#initial setup code
	imageDirectory = get_image_directory()
	cards_directory = imageDirectory + "/Cards/"
	maps_directory = imageDirectory + "/Maps/"
	
	
	#Card methods
	UIcards = []
	
	def remove_card(self):
		player = get_current_player()
		if player.has_taken_card:
			return
		costs = [0,1,1,2,2,3]
		n = int(self.sender().text()) - 1
		card = cards.pop(n)
		player.addCard(card)
		player.removeCoins(costs[n])
	
	def update_card_images(self):
		for i in range(6):
			try:
				image_name = cards[i].name.replace(" ","")
				icon = "%s%s.jpeg" % (self.cards_directory, image_name)
				self.UIcards[i].setPixmap(QtGui.QPixmap(icon))
			except IndexError:
				for p in players:
					print p
				sys.exit()
	
	
	
	#UI setup methods
	def cards_row(self):
		row = QtGui.QHBoxLayout()
		
		for i in range(6):
			card = QtGui.QLabel(self)
			self.UIcards.append(card)
			image_name = cards[i].name.replace(" ","")
			row.addWidget(self.UIcards[-1])
			#see if moving the QLabel along with the card works
		self.update_card_images()
		
		return row
	
	def card_buttons(self):
		card_selector = QtGui.QHBoxLayout()
		for i in range(6):
			card_button = QtGui.QPushButton(str(i+1), self)
			card_button.clicked.connect(self.remove_card)
			card_button.clicked.connect(self.update_card_images)
			card_selector.addWidget(card_button)
		return card_selector
	
	def get_maps(self):
		maps = []
		
		for i in range(4):
			map = QtGui.QLabel(self)
			maps.append(map)
			icon = QtGui.QPixmap(self.maps_directory + "map%s-A.png" % str(i))
			maps[-1].setPixmap(icon)
			
		return maps
	
	def map_grid(self):
		maps_etc = QtGui.QGridLayout()
		
		maps = self.get_maps()
		for i in range(3):
			maps_etc.addWidget(maps[i], 0, i)
		maps_etc.addWidget(maps[3], 1, 1)
		
		
		
		subVone = QtGui.QVBoxLayout()
		
		card_selector = self.card_buttons()
		
		
		#textArea = QtGui.QLabel(self)
		#textArea.setText("example text for whatever")
		
		print_p_btn = QtGui.QPushButton('Print Player', self)
		print_p_btn.clicked.connect(print_current_player)
		
		subVone.addLayout(card_selector)
		subVone.addWidget(print_p_btn)
		
		
		subVtwo = QtGui.QVBoxLayout()
		quitbtn = QtGui.QPushButton('Quit', self)
		quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		EndTurnbtn = QtGui.QPushButton('End Turn', self)
		EndTurnbtn.clicked.connect(self.end_turn)
		
		
		
		subVtwo.addWidget(quitbtn)
		subVtwo.addWidget(EndTurnbtn)
		
		maps_etc.addLayout(subVone, 1, 0)
		maps_etc.addLayout(subVtwo, 1, 2)
		
		return maps_etc
	
	def layoutSetup(self):
		vertical = QtGui.QVBoxLayout()
		vertical.addLayout(self.cards_row())
		vertical.addLayout(self.map_grid())
		self.setLayout(vertical)
	
	
	
	#Non-UI methods
	def end_turn(self):
		change_player()
	
	def __init__(self):
		super(boardGUI, self).__init__()
		self.initModel()
		self.initUI()
	
	
	def initModel(self):
		populate_cards()
		populate_players()
		
		
		
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
