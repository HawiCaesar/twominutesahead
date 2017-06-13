"""
This is a very simple game of choices. You have '2 minute head start' on you enemy.
You can only see 2 minutes ahead of them before they can attack you or you can block or make other decisions
"""

#class player(object):

class Enemy(object):
	 
	 def __init__(self, enemy_type, sound, number_of_enemies):
	 	self.sound = sound
	 	self.enemy_type = enemy_type
	 	try:
	 		self.number_of_enemies = int(number_of_enemies)
	 	except:
	 		raise TypeError("Number of Enemies should be an integer whole number")



	 def attack(self):
	 	if self.number_of_enemies == 1:
	 		print "There is %d %s behind you!\n %sing LOUDLY!!!" %(self.number_of_enemies, self.enemy_type, self.sound)

	 	elif self.number_of_enemies > 1:
	 		print "There are %d %ss coming towards you!\n %sing LOUDLY!!!" %(self.number_of_enemies, self.enemy_type, self.sound)

	 	else:
	 		print "You are a lucky today they are not coming for you!"



class Troll(Enemy):
	def __init__(self, enemy_type, sound, number_of_enemies):
		self.sound = sound
	 	self.enemy_type = enemy_type
	 	self.number_of_enemies = number_of_enemies

		super(Enemy, self).__init__()


class FlyingBat(Enemy):
	def __init__(self, enemy_type, sound, number_of_enemies):
		super(Enemy, self).__init__()


troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1)

troll.attack()