#!/usr/bin/env python

cardEffects = ["+1 flight", "+1 army", "+1 movement", "+1 VP per matching type", "+4 VP for all three", "+3 VP for both", "+1 elixer", "+2 elixer", "+3 elixer", "attack immunity", "+2 coins"]

turnEffects = ["+2 movement", "+3 movement", "+4 movement", "+5 movement", "+6 movement", "+1 castle", "+1 army", "+2 army", "+3 army", "+4 army", "remove army"]

cards = ["Cursed Gargoyles", "Ancient Woods", "Arcane Temple", "Cursed Banchee", "Ancient Tree Spirit", "Arcane Manticore", "Ancient Sage", "Ancient Phonix", "Arcane Sphinx", "Forest Lake ", "Dire Eye", "Cursed Tower", "Dire Ogre", "Dire Giant", "Cursed Mausoleum", "Dire Goblin", "Dire Dragon", "Cursed King", "Night Village", "Noble Knight", "Forest Tree Town", "Night Hydra", "Noble Hills", "Forest Gnome", "Noble Unicorn", "Cursed Graveyard", "Forest Elf", "Forest Pixie", "Mountain Treasury", "White Castle", "Mountain Dwarf", "Dire Stronghold", "Whiter Castle", "Night Wizard"]

class castle:
	def __init__(self, playerNumber):
		self.owner = playerNumber

class army:
	def __init__(self, playerNumber):
		self.owner = playerNumber

class location:
	def __init__(self, startingArmies, startingToken): #startingArmies = array of armies
		self.armies = startingArmies
		self.token = startingToken
	
	def removeArmy(playerNumber):
		for i in len(armies):
			if armies[i].owner == playerNumber:
				armies.remove(armies[i])
				break
	
	def addArmy(playerNumber):
		armies.add(army(playerNumber))
	
	def addCastle(playerNumber):
		self.castle = castle(playerNumber)
		
class card:
	def __init__(self, cardName, turnEffect, exclucive, turnEffect2, cardEffect, cardEffect2):
		self.name = cardName
		self.turnE = turnEffect
		self.both = exclusive
		self.turnE2 = turnEffect2
		self.cardE = cardEffect
		self.cardE2 = cardEffect2
		self.type = cardName.split(" ")[0]
		
		
class player:
	def __init__(self, playerNumber, startingArmies, startingCoins): #startingArmies = number of armies, ditto for coins
		self.id = playerNumber
		self.armies = startingArmies
		self.coins = startingCoins
		self.cards = []
	
	def removeArmy():
		self.armies -= 1
	
	def addArmy():
		self.armies += 1
	
	def removeCoin():
		self.coins -= 1
	
	def addCoin():
		self.coins += 1
	
	def addCard(card): #card object
		cards.append(card)