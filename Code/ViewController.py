#!/usr/bin/env python
import sys
import os
import random
from PySide import *
import Model
import Cards
import Maps
import Subclasses

"""
#OS X 10.9
#using PySide 1.2.1
#using Qt 4.8.6
#chmod +x this file, then cd [wherever this is], ./Risk2210.py
"""

#pulled from:
#https://wiki.python.org/moin/PyQt/Making%20non-clickable%20widgets%20clickable
#had to modify to work with pyside not pyqt
def clickable(widget):
    class Filter(QtCore.QObject):
        clicked = QtCore.Signal(QtCore.QObject)
        
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit(obj)
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
	#print old_player
	b = current_player + 1
	current_player = b if b < len(players) else 0

def populate_players():
	for i in range(4):
		players.append(Model.player(i, 9))

def print_current_player():
	print players[current_player].turn_print()

cards = []

def get_image_directory():
	folder = os.path.dirname(os.path.abspath(__file__))
	folders = folder.split("/")
	topics_folder = "/".join(folders[0:-2])
	image_folder = topics_folder + "/Image Resources/"
	return image_folder

def populate_cards():
	global cards
	cards = map(lambda c: Model.card(c).get(), Cards.get_cards())
	random.shuffle(cards)



class boardGUI(QtGui.QWidget): #cannot be QtGui.QMainWindow or button layout fails
	#initial setup code
	text_bar = -1
	imageDirectory = get_image_directory()
	cards_directory = imageDirectory + "/Cards/"
	maps_directory = imageDirectory + "/Maps/"
	map_objects = []
	
	def update_text_bar(self):
		self.text_bar.setText("Current Player: %s" % current_player)
	
	
	#map methods
	
	selected_territory = 0
	
	def click_on_map(self, map):
		player = get_current_player()
		
		def add_army_to_location():
			clicked_location.add_army(player.id)
			player.armies -= 1
			selected_territory = 0
		
		def print_loc_info():
			printout = (clicked_map_index, clicked_loc_index, clicked_location.armies)
			print "map index: %s location index: %s armies: %s" % printout
		
		def move_armies():
			#selecting a territory
			if self.selected_territory == 0:
				if clicked_location.armies[player.id] < 1:
					print "select a territory that has your armies"
					return
				else:
					self.selected_territory = [clicked_map_index,clicked_loc_index]
					
					
					
			#moving the army
			else:
				s = self.selected_territory
				move_from_loc = self.map_objects[s[0]].map_locations[s[1]]
				move_from_map_index = s[0]
				e_borders = move_from_loc.external_borders
				
				if clicked_map_index == move_from_map_index: #on same map
					if clicked_loc_index in move_from_loc.land_borders:
						move_from_loc.armies[player.id] -= 1
						clicked_location.armies[player.id] += 1
						self.selected_territory = 0
						player.move -= 1
					elif clicked_loc_index in move_from_loc.sea_borders:
						if player.move < player.waterMovement: return
						move_from_loc.armies[player.id] -= 1
						clicked_location.armies[player.id] += 1
						self.selected_territory = 0
						player.move -= player.waterMovement
				
				elif e_borders != []:
					valid = False
					
					if player.move < player.waterMovement: return
					east,north,west,south = [0,1,2,3]
					#external borders: ENWS, 0,1,2,3
					#need to check if clicked location has correct external border
					#get correct map for from border, check against clicked
					#get opposite direction border, check if location has that border
					if move_from_map_index == 0 and east in e_borders: #left, east
						if clicked_map_index == 1:
							if west in clicked_location.external_borders:
								valid = True
					elif move_from_map_index == 2 and west in e_borders: #right, west
						if clicked_map_index == 1:
							if east in clicked_location.external_borders:
								valid = True
					elif move_from_map_index == 3 and north in e_borders: #bottom, north
						if clicked_map_index == 1:
							if south in clicked_location.external_borders:
								valid = True
					elif move_from_map_index == 1: # center map
						if clicked_map_index == 0 and west in e_borders:
							if east in clicked_location.external_borders:
								valid = True
						if clicked_map_index == 2 and east in e_borders:
							if west in clicked_location.external_borders:
								valid = True
						if clicked_map_index == 3 and south in e_borders:
							if north in clicked_location.external_borders:
								valid = True
					
					if not valid: return
					
					move_from_loc.armies[player.id] -= 1
					clicked_location.armies[player.id] += 1
					self.selected_territory = 0
					player.move -= player.waterMovement
		
		def add_castle_to_location():
			if clicked_location.armies[current_player] < 1:
				return
			if clicked_location.castle[0] is not 0:
				return
			clicked_location.castle = [current_player]
			player.castle -= 1
			selected_territory = 0
		
		clicked_map_index = map.map_index
		clicked_location = -1
		clicked_loc_index = -1
		
		
		mouseXY = map.mapFromGlobal(QtGui.QCursor.pos()) #qpoint
		num_locations = len(map.map_locations)
	
		for loc in map.map_locations:
			if (loc.center - mouseXY).manhattanLength() < loc.radius:
				clicked_loc_index = map.map_locations.index(loc)
				#manhattanL is |x|+|y|, much easier than sqrt
				#you get a diamond not a circle, but whatever
				clicked_location = loc
				break
		if clicked_loc_index is -1:
			print "not within location"
			return
		
		if player.armies > 0:
			add_army_to_location()
		elif player.move > 0:
			move_armies()
		elif player.castle > 0:
			add_castle_to_location()
				
		
		self.printout()
	
	
	
	
	
	def calculate_winner(self):
		os.system('clear')
		victory_points = [0,0,0,0]
		
		#area control
		for m in self.map_objects:
			for location in m.map_locations:
				most_armies = max(location.armies)
				if location.armies.count(most_armies) > 1:
					continue
				victory_points[location.armies.index(most_armies)] += 1
		
		#cards
		for index in range(4): #players
			player = players[index]
			cards = str(player.cards)
			count = 0
			for type in player.vp_categories:
				if type == "3":
					count += player.coins//3
				elif type == "all":
					if cards.count("Noble") == 3: count += 4
				elif type == "both":
					if cards.count("Mountain") == 2: count += 3
				else:
					count += cards.count(type)
			victory_points[index] += count
		
		#elixer
		elixers = map(lambda x: x.get_elixer(), players)
		victory_points[elixers.index(max(elixers))] += 2
			
			
			
		print "Player %s is the Winner!!" % victory_points.index(max(victory_points))
		sys.exit()
	
	
	
	#Card methods
	UIcards = []
	
	def remove_card(self):
		player = get_current_player()
		if player.has_taken_card:
			return
		costs = [0,1,1,2,2,3]
		n = int(self.sender().text()) - 1
		if player.coins < costs[n]:
			print "not enough coins"
			return
		card = cards.pop(n)
		player.addCard(card)
		player.removeCoins(costs[n])
		self.printout()
	
	def update_card_images(self):
		for i in range(6):
			try:
				image_name = cards[i].name.replace(" ","")
				icon = "%s%s.jpeg" % (self.cards_directory, image_name)
				self.UIcards[i].setPixmap(QtGui.QPixmap(icon))
			except IndexError:
				self.calculate_winner()
	
	
	#UI setup methods
	
	def cards_row(self):
		row = QtGui.QHBoxLayout()
		
		for i in range(6):
			card = QtGui.QLabel(self)
			self.UIcards.append(card)
			#image_name = cards[i].name.replace(" ","")
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
		for i in range(4):
			map = Subclasses.Map(maps[i], i)
			icon = QtGui.QPixmap("%s%s.png" % (self.maps_directory, maps[i][0]))
			map.setPixmap(icon)
			clickable(map).connect(self.click_on_map)
			self.map_objects.append(map)
			
		return self.map_objects
	
	def left_info_area(self):
		subVone = QtGui.QVBoxLayout()
		
		card_selector = self.card_buttons()
		
		
		textArea = QtGui.QLabel(self)
		textArea.setText("Current Player: 0")
		self.text_bar = textArea
		
		text_btn = QtGui.QPushButton('Update Output', self)
		text_btn.clicked.connect(self.printout)
		
		subVone.addLayout(card_selector)
		subVone.addWidget(textArea)
		subVone.addWidget(text_btn)
		
		return subVone
		
	def right_info_area(self):
		#right info area
		subVtwo = QtGui.QVBoxLayout()
		quitbtn = QtGui.QPushButton('Quit', self)
		#quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		quitbtn.clicked.connect(self.calculate_winner)
		
		EndTurnbtn = QtGui.QPushButton('End Turn', self)
		EndTurnbtn.clicked.connect(self.end_turn)
		
		subVtwo.addWidget(quitbtn)
		subVtwo.addWidget(EndTurnbtn)
		
		return subVtwo
	
	def map_grid(self):
	
		maps_etc = QtGui.QGridLayout()
		
		#main maps
		maps = self.get_maps()
		for i in range(4):
			y = i//3
			x = i%3 + y
			maps_etc.addWidget(maps[i], y, x)
		
		
		#adding stuff
		maps_etc.addLayout(self.left_info_area(), 1, 0)
		maps_etc.addLayout(self.right_info_area(), 1, 2)
		
		return maps_etc
	
	def layoutSetup(self):
		vertical = QtGui.QVBoxLayout()
		vertical.addLayout(self.cards_row())
		vertical.addLayout(self.map_grid())
		self.setLayout(vertical)
	
	
	def print_board(self):
		locales = ["left  ","center","right ","bottom"]
		for i in range(len(self.map_objects)):
			map = self.map_objects[i]
			for k in range(len(map.map_locations)):
				location = map.map_locations[k]
				printout = (k, locales[i], location.armies, location.castle)
				print "armies at location %s on %s map: %s. Castle owner: %s" % printout
			print
	
	def print_players(self):
		print get_current_player().turn_print()
		for player in players:
			print player
	
	def printout(self):
		self.update_text_bar()
		os.system('clear')
		self.print_players()
		self.print_board()
		print "Current Selected Territory: %s" % self.selected_territory
		
	
	
	#Non-UI methods
	def end_turn(self):
		current_player = get_current_player()
		if not current_player.has_taken_card:
			print "please take a card"
			return
		change_player()
		self.printout()
			
	def __init__(self):
		super(boardGUI, self).__init__()
		self.initUI()
		
		
	def initUI(self):
		populate_cards()
		populate_players()
		self.layoutSetup()
		self.setWindowTitle('Eight Minute Empire: Legends')
		#self.setWindowIcon(QtGui.QIcon('web.png'))		this for title bar
		self.move(200,200)
		self.map_objects[1].map_locations[0].armies = [4,4,4,4]
		self.map_objects[0].map_locations[0].armies = [1,1,1,1]
		self.printout()
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