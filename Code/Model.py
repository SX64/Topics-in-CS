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

class player:
	def __init__(self, playerNumber, startingArmies, startingCoins): #startingArmies = number of armies, ditto for coins
		self.id = playerNumber
		self.armies = startingArmies
		self.coins = startingCoins
		self.cards = []
		self.waterMovement = 3
		self.baseArmies = 0
		self.baseMovement = 0
		self.elixer = 0
	
	def applyCardEffects(card):
		effect = card.cardE.split(" ")
		if effect[-1] == "army":
			self.armies += int(effect[0])
		elif effect[-1] == "flight":
			self.waterMovement -= int(effect[0])
		elif effect[-1] == "movement":
			self.baseMovement += int(effect[0])
		elif effect[-1] == "type":
			return
		elif effect[-1] == "three":
			return
		elif effect[-1] == "both":
			return
		elif effect[-1] == "elixer":
			self.elixer += int(effect[0])
		elif effect[-1] == "immunity":
			return
		elif effect[-1] == "coins":
			self.coins += int(effect[0])
	
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