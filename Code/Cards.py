#order is: cardName, turnEffect, turnEffect2, both, cardEffect, cardEffect2
#turn effects at bottom of card

both,pick_one,n = True,False,"null"

card_definition = [
["Cursed Gargoyles","5 move",n,pick_one,"1 fly",n],
["Ancient Woods","1 castle","1 army",both,"1 army",n],
["Arcane Temple","3 move",n,pick_one,"1 VP per Arcane",n],
["Cursed Banshee","6 move",n,pick_one,"2 elixer",n],
["Ancient Tree Spirit","4 army",n,pick_one,"3 elixer",n],
["Arcane Manticore","4 army","remove army",both,"one move",n],
["Ancient Sage","3 move",n,pick_one,"1 VP per Ancient",n],
["Ancient Phoenix","5 move",n,pick_one,"1 fly",n],
["Arcane Sphinx","3 army","4 move",pick_one,"1 fly",n],
["Forest Lake","2 army","3 move",pick_one,"1 VP per Forest",n],
["Dire Eye","4 army",n,pick_one,"fly",n],
["Cursed Tower","1 castle",n,pick_one,"1 VP per Flight",n],
["Dire Ogre","2 move",n,pick_one,"1 VP per 3 Coins",n],
["Dire Giant","3 army","remove army",both,"attack immunity",n],
["Cursed Mausoleum","1 castle",n,pick_one,"1 move",n],
["Dire Goblin","5 move",n,pick_one,"1 elixer",n],
["Dire Dragon","3 army","remove army",both,"fly",n],
["Cursed King","3 army","4 move",pick_one,"1 elixer",n],
["Night Village","1 castle",n,pick_one,"1 army",n],
["Noble Knight","4 army","remove army",both,"1 move",n],
["Forest Tree Town","1 castle",n,pick_one,"1 move",n],
["Night Hydra","5 move","remove army",both,"1 army",n],
["Noble Hills","3 army",n,pick_one,"4 VP for all Noble",n],
["Forest Gnome","2 move",n,pick_one,"3 elixer",n],
["Noble Unicorn","4 move","army",both,"1 move",n],
["Cursed Graveyard","2 army",n,pick_one,"1 VP per Cursed",n],
["Forest Elf","3 army","2 move",pick_one,"1 army",n],
["Forest Pixie","4 move",n,pick_one,"1 army",n],
["Mountain Treasury","3 move",n,pick_one,"1 elixer","2 coin"],
["White Castle","3 army","1 castle",pick_one,"1 elixer",n],
["Mountain Dwarf","2 army","remove army",both,"3 VP for both Mountain",n],
["Dire Stronghold","1 castle",n,pick_one,"1 VP per Dire",n],
["Whiter Castle","3 move","1 castle",both,"1 elixer",n],
["Night Wizard","3 army","remove army",both,"1 VP per Night",n]
]

def get_cards():
	return card_definition