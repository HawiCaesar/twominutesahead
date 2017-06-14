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
        return "YOU BETTER THINK QUICKLY AND DEFEND YOURSELF!!!"

    def scare(self):
        return "YOU BETTER THINK QUICKLY"


# Inherit from Enemy
class Troll(Enemy):
    def __init__(self, enemy_type, sound, number_of_enemies, damage):
        super(Troll, self).__init__()
        super(Troll, self).set_enemy(enemy_type, sound, number_of_enemies, damage)

        self.trolls_around_player = super(Troll, self).get_number_of_enemies()
        self.troll_type = super(Troll, self).get_enemy_type()
        self.troll_sound = super(Troll, self).get_sound()
        self.troll_damage = super(Troll, self).get_damage()

    def scare(self):
        return self.troll_sound +"!!!!\n "+ super(Troll, self).scare()

    def attack(self):
        if  self.trolls_around_player == 1:
            print "The %s attacks you and you are in pain!!! -%d of your life" %(self.troll_type, self.troll_damage)

        elif self.trolls_around_player > 1:
            print "The %ss attack you and you are in pain REAL PAIN!!! -%d of your life" %(self.troll_type, self.troll_damage)

        return super(Troll, self).attack()



# Inherit from Enemy
class FlyingBat(Enemy):
    def __init__(self, enemy_type, sound, number_of_enemies, damage):
        super(FlyingBat, self).__init__()
        super(FlyingBat, self).set_enemy(enemy_type, sound, number_of_enemies, damage)

        self.bats_around_player = super(FlyingBat, self).get_number_of_enemies()
        self.bats_type = super(FlyingBat, self).get_enemy_type()
        self.bats_sound = super(FlyingBat, self).get_sound()
        self.bats_damage = super(FlyingBat, self).get_damage()

    def scare(self):
        return self.bats_sound +"!!!!\n "+ super(FlyingBat, self).attack()

    def attack(self):
        if  self.bats_around_player == 1:
            print "The %s attacks you, sucking your blood and you are in pain!!! -%d of your life" %(self.bats_type, self.bats_damage)

        elif self.bats_around_player > 1:
            print "The %ss attack by sucking your blood! -%d of your life" %(self.bats_type, self.bats_damage)

        return super(FlyingBat, self).attack()



#troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 40)
#print(troll.scare())


def main():

    print "You are an exception individual. You can see at least 2 minutes into the future"
    print "You are walking in a forest and if have this 'see into the future moment' "
    print "You see a Troll a head of you and you also see bats flying from behind you"
    choice = raw_input("What do you do? Answer 1 for facing the Troll and 2 flying bats ")

    if choice == "1":
        print "You can magically summon weapons!"

        weapon_choice_one = raw_input("Answer 1 for Sword  and 2 for Big Guns ? \n")

        if weapon_choice_one == "1":
            player1 = Player()
            player1.set_weapon('Sword')

            print "I will use the " +player1.get_weapon()+ ". \n"+player1.ready()

            troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 41)
            print troll.scare()

            choice2 = raw_input("What do you do?  1 for Attack or 2 to let it come first \n")

            if choice2 =="1":
                print "You are GREAT! You slay the BEAST"

            elif choice2 == "2":
                print troll.attack()
                print(player1.player_life - troll.get_damage())

                print "It finds a way to hurt you but in the end YOU WIN!!!!"
            else:
                print "You let it Kill you!!!"

        elif weapon_choice_one == "2":
            troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 41)
            print troll.scare()

            choice_gun = raw_input("What do you do?  1 for Attack or 2 to let it come first\n")

            if choice_gun == "1":
                print "You are GREAT! You shoot the BEAST vigorously"
            elif choice_gun == "2":
                print troll.attack()
                print(player1.player_life - troll.get_damage())

                print "It hits you  badly but in the end YOU WIN!!!!"
            else:
                print "You let it Kill you!!!"

        else:
            print "You shoud have chosen a weapon! Now they will suck your bones dry"

    elif choice == "2":

        print "You can magically summon weapons!"
        
        weapon_choice_two = raw_input("Answer 1 for Flamethrower and 2 for Ray Gun\n")

        if weapon_choice_two == "1":
            player1 = Player()
            player1.set_weapon('Flamethrower')

            print "I will use the " +player1.get_weapon()+ ". \n"+player1.ready()

            bat = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 40, 5)
            print bat.scare()

            choice_bats = raw_input("What do you do?  1 for Attack or 2 to let it come first\n")

            if choice_bats == "1":
                print "You Burn all the bats!! GREAT"
            elif choice_bats == "2":

                print bat.attack()
                print(player1.player_life - bat.get_damage())

                print "They overwelm you but in the end YOU WIN!!!!"
            else:
                print "They Killed you!!!"

        elif weapon_choice_two == "2":
            player1 = Player()
            player1.set_weapon('Ray Gun')
            
            print "I will use the " +player1.get_weapon()+ ". \n"+player1.ready()

            bat = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 40, 5)
            bat.scare()

            choice_bats = raw_input("What do you do?  1 for Attack or 2 to let it come first\n")

            if choice_bats == "1":
                print "You Kill all the bats GREAT"
            elif choice_bats == "2":

                print bat.attack()
                print(player1.player_life - bat.get_damage())

                print "They overwelm you but in the end YOU WIN thanks to the Ray Gun!!!!"
            else:
                print "They Killed you!!!"

    else:
        print "You shoud have made a Choice! Now they will suck your bones dry"


if __name__ == '__main__':
    main()





