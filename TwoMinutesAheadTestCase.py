import unittest 

from twominutesahead import Enemy, Troll, FlyingBat, Player

class TwoMinutesAheadTestCase(unittest.TestCase):

   # Check if Child Enemy classes are instances of Enemy class
   def test_troll_instance_of_enemy(self):
		troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 40)
		self.assertIsInstance(troll, Enemy, msg='The object should be an instance of the `Enemy` class')

   def test_flying_instance_of_enemy(self):
		bats = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 35, 5)
		self.assertIsInstance(bats, Enemy, msg='The object should be an instance of the `Enemy` class')

   
   # Check if player is in game when initialised
   def test_player_is_in_game(self):
		player1 = Player()
		self.assertEqual(player1.ready(), "I'm Ready, Bring It!", "Player has not entered the game properly")

   #Check if player has weapon set and ready
   def test_player_weapon_is_set_and_ready(self):
      player1 = Player()
      player1.set_weapon('sword')
      self.assertEqual(player1.get_weapon, 'sword', "Player has no weapon")


   

   


