import unittest 

from twominutesahead import Enemy, Troll, FlyingBat, Player

class TwoMinutesAheadTestCase(unittest.TestCase):

	#Check if Troll and Flying bat are instances of Enemy
   	def test_troll_instance_of_enemy(self):
   		troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 40)
   		self.assertIsInstance(troll, Enemy, msg='The object should be an instance of the `Enemy` class')


   	def test_flying_instance_of_enemy(self):
   		bats = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 35, 5)
   		self.assertIsInstance(bats, Enemy, msg='The object should be an instance of the `Enemy` class')

   	# Check if zero enemies are brought to the game
   	def test_enemy_objects_is_zero(self):
   		troll = Troll('Short-Snout-Troll', 'ROAAAAR', 0, 0)
		self.assertEqual(troll.scare(), "You are a lucky today they are not coming for you!", "No enemies for the moment")

	def test_player_is_in_game(self):
		player1 = Player('sword')
		self.assertEqual(player1.ready(), "I'm Ready, Bring It!", "Player has entered the game")

	def test_enemy_can_attack(self):
		manbat = FlyingBat('Swedish Bat', 'Screech-Screech-SCREECH', 32, 6)
		self.assertEqual(manbat.attack(), "YOU BETTER THINK QUICKY AND GET OUT OF THERE!!!", "attack method should communicate to user")



