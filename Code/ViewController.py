#!/usr/bin/env python
import sys
import os
import random
from PySide import *
import Model
import Cards
import Maps
import ButtonExtension

"""
#OS X 10.9
#using PySide 1.2.1
#using Qt 4.8.6
#chmod +x this file, then cd [wherever this is], ./Risk2210.py
"""

def clickable(widget):

    class Filter(QObject):
    
        clicked = pyqtSignal()
        
        def eventFilter(self, obj, event):
        
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


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
	def get_click_location(self):
		print "spleen"
	
	def get_button_location(self):
		pushed_button = self.sender()
		print pushed_button.location_info
	
	def buttons_grid(self,num):
		scale_options = [[8,12,12,0],[10,15,12,0],[20,30,10,0]]
		scaling = 0
		flat_buttons = True
		image_size = [300,200] #x,y
		num_buttons_vertical = scale_options[scaling][0]
		num_buttons_horizontal = scale_options[scaling][1]
		
		
		
		button_width = Maps.maps_image_size[0]//num_buttons_horizontal +1
		button_height = Maps.maps_image_size[1]//num_buttons_vertical
		#one pixel border around buttons, not sure why only horizontal
		button_spacing = scale_options[scaling][2 if not flat_buttons else 3]
		#no idea why the flat/not flat spacing difference
		
		button_grid = QtGui.QGridLayout()
		button_grid.setHorizontalSpacing(button_spacing)
		button_grid.setVerticalSpacing(button_spacing)
		
		
		for i in range(num_buttons_vertical):
			for j in range(num_buttons_horizontal):
				location_list = [num,i,j]
				button = ButtonExtension.SuperButton(location_list,'',self)
				button.setFlat(flat_buttons)
				button.setMaximumWidth(button_width)
				button.setMaximumHeight(button_height)
				button.clicked.connect(self.get_button_location)
				button_grid.addWidget(button, i, j)
				
		
		#experimental, currently slower than nested loop
		"""
		for x in range(num_buttons_vertical*num_buttons_horizontal):
			i = x//num_buttons_horizontal
			j = x%num_buttons_horizontal
			location_list = [num,i,j]
			button = ButtonExtension.SuperButton(location_list,'',self)
			button.setFlat(flat_buttons)
			button.setMaximumWidth(button_width)
			button.setMaximumHeight(button_height)
			button.clicked.connect(self.alternate_button_location)
			button_grid.addWidget(button, i, j)"""
		
		return button_grid
	
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
			card_button.setMaximumWidth(45)
			card_button.clicked.connect(self.remove_card)
			card_button.clicked.connect(self.update_card_images)
			card_selector.addWidget(card_button)
		return card_selector
	
	def get_maps(self):
		maps = Maps.get_maps()
		random.shuffle(maps)
		map_images = []
		for i in range(4):
			map = QtGui.QLabel(self)
			map_images.append(map)
			#icon = QtGui.QPixmap(self.maps_directory + "map%s-A.png" % str(i))
			icon = QtGui.QPixmap("%s%s.png" % (self.maps_directory, maps[i][0]))
			map_images[-1].setPixmap(icon)
			
		return map_images
	
	def map_grid(self):
		maps_etc = QtGui.QGridLayout()
		
		
		#main maps
		maps = self.get_maps()
		for i in range(4):
			#grid = self.buttons_grid(i)
			y = i//3
			x = i%3 + y
			maps_etc.addWidget(maps[i], y, x)
			#maps_etc.addLayout(grid, y, x)
		
		
		#left info area
		subVone = QtGui.QVBoxLayout()
		
		card_selector = self.card_buttons()
		
		
		#textArea = QtGui.QLabel(self)
		#textArea.setText("example text for whatever")
		
		print_p_btn = QtGui.QPushButton('Print Player', self)
		print_p_btn.clicked.connect(print_current_player)
		
		subVone.addLayout(card_selector)
		subVone.addWidget(print_p_btn)
		
		#right info area
		subVtwo = QtGui.QVBoxLayout()
		quitbtn = QtGui.QPushButton('Quit', self)
		quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		EndTurnbtn = QtGui.QPushButton('End Turn', self)
		EndTurnbtn.clicked.connect(self.end_turn)
		
		subVtwo.addWidget(quitbtn)
		subVtwo.addWidget(EndTurnbtn)
		
		
		#adding stuff
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
