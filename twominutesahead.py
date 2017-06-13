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
	 		print "There is %d %s ahead you!\n %sing LOUDLY!!!" %(self.number_of_enemies, self.enemy_type, self.sound)

	 	elif self.number_of_enemies > 1:
	 		print "There are %d %ss coming towards you!\n %sing LOUDLY!!!" %(self.number_of_enemies, self.enemy_type, self.sound)

	 	else:
	 		return "You are a lucky today they are not coming for you!"

	 def attack(self):
	 	if self.number_of_enemies == 1:
	 		print "The %s attacks you and you are in pain!!! -%d " %(self.enemy_type, self.damage)

	 	elif self.number_of_enemies > 1:
	 		print "The %ss attack you and you are in pain REAL PAIN!!! -%d of your life" %(self.enemy_type, self.damage)

	 	return "YOU BETTER THINK QUICKLY AND GET OUT OF THERE!!!"




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



"""
print "You are an exception individual. You can see at least 2 minutes into the future"
print "You are walking in a forest and if have this 'see into the future moment' "
print "You see a Troll a head of you and you also see bats flying from behind you"
choice = raw_input("What do you do? Answer 1 for facing the Troll and 2 flying bats ")

if choice == "1":
	print "You can magically summon weapons!"

	weapon_choice_one = raw_input("Answer 1 for Sword  and 2 for Big Guns ?")

	if weapon_choice_one == "1":
		player1 = Player('sword')
		player1.ready()

		troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 41)
		troll.scare()

		choice2 = raw_input("What do you do?  1 for Attack or 2 to let it come first")

		if choice2 =="1":
			print "You are GREAT! You slay the BEAST"
		elif choice2 == "2":
			troll.attack()
			print(player1.player_life - troll.damage)

			print "It finds a way to hurt you but in the end YOU WIN!!!!"
		else:
			print "You let it Kill you!!!"

	elif weapon_choice_one == "2":
		troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 41)
		troll.scare()

		choice_gun = raw_input("What do you do?  1 for Attack or 2 to let it come first")

		if choice_gun == "1":
			print "You are GREAT! You shoot the BEAST vigorously"
		elif choice_gun == "2":
			troll.attack()
			print(player1.player_life - troll.damage)

			print "It hits you  badly but in the end YOU WIN!!!!"
		else:
			print "You let it Kill you!!!"

	else:
		print "You shoud have chosen a weapon! Now they will suck your bones dry"

elif choice == "2":

	weapon_choice_two = raw_input("Answer 1 for Flamethrower and 2 for Ray Gun")

	if weapon_choice_two == "1":
		player1 = Player('Flamethrower')
		player1.ready()

		bat = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 40, 5)
		bat.scare()

		choice_bats = raw_input("What do you do?  1 for Attack or 2 to let it come first")

		if choice_bats == "1":
			print "You Burn all the bats!! GREAT"
		elif choice_bats == "2":

			bat.attack()
			print(player1.player_life - bat.damage)

			print "They overwelm you but in the end YOU WIN!!!!"
		else:
			print "They Killed you!!!"

	elif weapon_choice_two == "2":
		player1 = Player('Ray Gun')
		player1.ready()

		bat = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 40, 5)
		bat.scare()

		choice_bats = raw_input("What do you do?  1 for Attack or 2 to let it come first")

		if choice_bats == "1":
			print "You Kill all the bats GREAT"
		elif choice_bats == "2":

			bat.attack()
			print(player1.player_life - bat.damage)

			print "They overwelm you but in the end YOU WIN thanks to the Ray Gun!!!!"
		else:
			print "They Killed you!!!"

else:
	print "You shoud have made a Choice! Now they will suck your bones dry"

"""



