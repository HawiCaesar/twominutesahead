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
	 	if self.number_of_enemies > 1:
	 		print("There is %d "+self.enemy_type+" behind you!\n It is "+self.sound+"ing LOUDLY ", self.number_of_enemies)

	 	else:
	 		print("There are %d "+self.enemy_type+"s walking towards you!\n They are all "+self.sound+"ing LOUDLY ", self.number_of_enemies)




class Troll(Enemy):
	def __init__(self, enemy_type, sound, number_of_enemies):
		super(Enemy, self).__init__()


class FlyingBat(Enemy):
	def __init__(self, enemy_type, sound, number_of_enemies):
		super(Enemy, self).__init__()