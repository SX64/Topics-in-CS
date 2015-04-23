from PySide import *
class SuperButton(QtGui.QPushButton):
	location_info = "null"
	def __init__(self, location_list, text = '', parent = None):
		self.location_info = location_list
		QtGui.QPushButton.__init__(self, text, parent)




class location:
	def __init__(self, data_array):
		self.armies = [0,0,0,0]
		self.castle = [-1]
		self.center = QtCore.QPoint(data_array[0][0], data_array[0][1])
		self.radius = data_array[0][2]
		self.land_borders = data_array[1]
		self.sea_borders = data_array[2]
		self.external_borders = data_array[3]
	
	def add_army(self, player_index):
		self.armies[player_index] += 1
	
	def remove_army(self, player_index):
		pile = self.armies[player_index]
		if pile == 0:
			print "no armies to remove"
			return
		pile -= 1


class Map(QtGui.QLabel):
	def __init__(self, map_data_input, map_number):
		QtGui.QLabel.__init__(self)
		self.map_data = map_data_input
		self.map_index = map_number
		temp_locs = []
		for location_array in self.map_data[-1]:
			new_location = location(location_array)
			#if you do map_locations.append, bad things happen, don't know why
			temp_locs.append(new_location)
		self.map_locations = temp_locs