"""
This is a very simple game of choices. You have '2 minute head start' on you enemy.
You can only see 2 minutes ahead of them before they can attack you or you can block or make other decisions
"""

class Player(object):
	def __init__(self, weapon):
		self.weapon = weapon
		self.player_life = 100

	
	def ready(self):
		return "I'm Ready, Bring It!"




class Enemy(object):
	 
	 def __init__(self, enemy_type, sound, number_of_enemies, damage):
	 	self.sound = sound
	 	self.enemy_type = enemy_type
	 	

	 	try:
	 		self.number_of_enemies = int(number_of_enemies)
	 	except:
	 		raise TypeError("Number of Enemies should be an integer whole number")

	 	try:
	 		self.damage = int(damage)

	 	except:
	 		raise TypeError("Damage of enemies is a whole number")


	 def scare(self):
	 	if self.number_of_enemies == 1:
	 		print "There is %d %s behind you!\n %sing LOUDLY!!!" %(self.number_of_enemies, self.enemy_type, self.sound)

	 	elif self.number_of_enemies > 1:
	 		print "There are %d %ss coming towards you!\n %sing LOUDLY!!!" %(self.number_of_enemies, self.enemy_type, self.sound)

	 	else:
	 		return "You are a lucky today they are not coming for you!"

	 def attack(self):
	 	if self.number_of_enemies == 1:
	 		print "The %s attacks you and you are in pain!!! -%d " %(self.enemy_type, self.damage)

	 	elif self.number_of_enemies > 1:
	 		print "The %ss attack you and you are in pain REAL PAIN!!! -%d of your life" %(self.enemy_type, self.damage)

	 	return "YOU BETTER THINK QUICKY AND GET OUT OF THERE!!!"




class Troll(Enemy):
	def __init__(self, enemy_type, sound, number_of_enemies, damage):
		self.sound = sound
	 	self.enemy_type = enemy_type
	 	self.number_of_enemies = number_of_enemies
	 	self.damage = damage

		super(Enemy, self).__init__()


class FlyingBat(Enemy):
	def __init__(self, enemy_type, sound, number_of_enemies, damage):
		self.sound = sound
	 	self.enemy_type = enemy_type
	 	self.number_of_enemies = number_of_enemies
	 	self.damage = damage

		super(Enemy, self).__init__()


troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 41)

troll.scare()

