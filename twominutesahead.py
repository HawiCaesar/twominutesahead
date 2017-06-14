"""
This is a very simple game of choices. You have '2 minute head start' on you enemy.
You can only see 2 minutes ahead of them before they can attack you or you can block or make other decisions
"""

# Player class
class Player(object):

	def __init__(self):
		self.player_life = 100
		self.weapon = ""

		# private variable not accessible outside
		self.__entered_game = "I'm Ready, Bring It!" 

	def ready(self): 
		return self.__entered_game


	def set_weapon(self, weapon):
		self.weapon = weapon

	def get_weapon(self):
		return self.weapon



class Enemy(object):

    def __init__(self):
        self.__sound = ""
        self.__enemy_type = ""
        self.__number_of_enemies = 0
        self.__damage = 0
        self.__enemy_origin = "Magical Runes Forest"


    def set_enemy(self, enemy_type, sound, number_of_enemies, damage):
        self._enemy_type = enemy_type
        self._sound = sound
        self._number_of_enemies = number_of_enemies
        self._damage = damage

    #getter methods
    def get_number_of_enemies(self):
        return self._number_of_enemies

    def get_sound(self):
        return self._sound

    def get_enemy_type(self):
        return self._enemy_type

    def get_damage(self):
        return self._damage


    #Base class methods
    def attack(self):
        return "YOU BETTER THINK QUICKLY AND GET OUT OF THERE!!!"

    def scare(self):
        return "YOU BETTER THINK QUICKLY AND GET OUT OF THERE!!!"



class Troll(Enemy):
    def __init__(self, enemy_type, sound, number_of_enemies, damage):
        super(Troll, self).__init__()
        super(Troll, self).set_enemy(enemy_type, sound, number_of_enemies, damage)

    def scare(self):
        return super(Troll,self,).get_sound()




class FlyingBat(Enemy):
    def __init__(self, enemy_type, sound, number_of_enemies, damage):
        super(FlyingBat, self).__init__()

        super(FlyingBat, self).set_enemy(enemy_type, sound, number_of_enemies, damage)



troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 40)


print(troll.scare())





