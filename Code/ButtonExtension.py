from PySide import *
class SuperButton(QtGui.QPushButton):
	location_info = "null"
	def __init__(self, location_list, text = '', parent = None):
		self.location_info = location_list
		QtGui.QPushButton.__init__(self, text, parent)