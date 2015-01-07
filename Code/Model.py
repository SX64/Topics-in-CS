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


class card: #card effects are forever, turn effects only once
	def __init__(self, cardName, turnEffect, turnEffect2, both, cardEffect, cardEffect2):
		self.name = cardName
		self.turnE = turnEffect
		self.bothCardEffects = both
		self.turnE2 = turnEffect2
		self.cardE = cardEffect
		self.cardE2 = cardEffect2
		self.type = cardName.split(" ")[0]

	def __repr__(self):
		return self.name
	
#player poorly handles turn effects, requires rework
class player: #how this handles armies is inconsistent, discuss
	def __init__(self, playerNumber, startingArmies, startingCoins): #startingArmies = number of armies, ditto for coins
		self.id = playerNumber
		self.armies = startingArmies
		self.coins = startingCoins
		self.cards = []
		self.waterMovement = 3
		self.baseArmies = 0
		self.baseMovement = 0
		self.elixer = 0
	
	def addArmies(self, amount):
		self.armies += amount
	
	def addCoins(self, amount):
		self.coins += amount
	
	def applyTurnEffects(self, card): #currently assumes player always choses first option
		teffect = card.turnE.split(" ")
		type = teffect[1]
		value = int(teffect[0])
		if type == "army":
			return
		elif type == "move":
			return
		elif type == "castle":
			return
		
		if card.bothCardEffects is False:
			return
		
		teffect2 = card.turnE2.split(" ")
		type = teffect2[1]
		try:
			value = int(teffect2[0])
			if type == "army":
				return
			elif type == "move":
				return
			elif type == "castle":
				return
		except ValueError:
			#this is for remove army
			return
	
		
	def applyCardEffects(self, card): #only does first effect
		effect = card.cardE.split(" ")
		type = effect[1]
		if type == "immunity":
			return
		else:
			value = int(effect[0])
			if type == "army":
				self.baseArmies += value
			elif type == "fly":
				self.waterMovement -= value
			elif type == "move":
				self.baseMovement += value
			elif type == "elixer":
				self.elixer += value
			elif type == "coins":
				self.addCoins(value)
			elif type == "VP":
				return
			else:
				print "you forgot something"
			if card.cardE2 is not "null":
				self.addCoins(2)
	
	def removeArmies(self, amount):
		self.armies -= amount
	
	def removeCoins(self, amount):
		self.coins -= amount
	
	def addCard(self, card): #card object
		self.cards.append(card)
		self.applyTurnEffects(card)
		self.applyCardEffects(card)
		
	def __repr__(self):
		return "player %s:\narmies: %s\ncoins %s\ncards: %s\nmovement over water cost: %s\nadditional armies: %s\nadditional movement: %s\nelixer: %s" % (str(self.id), str(self.armies), str(self.coins), str(self.cards), str(self.waterMovement), str(self.baseArmies), str(self.baseMovement), str(self.elixer))