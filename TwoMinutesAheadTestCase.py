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
      self.assertEqual(player1.get_weapon(), 'sword', "Player has no weapon")

   # Check if Enemy:Troll makes sound
   def test_enemy_makes_sound(self):
      troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1, 40)
      self.assertEqual(troll.get_sound(), 'ROAAAAR', "Enemey:Troll does not make sound")

   # Check if Enemy:FlyingBat makes sound
   def test_enemy_makes_sound2(self):
      bat = FlyingBat('Blind-Bat', 'Screech-Screech-SCREECH', 45, 2)
      self.assertEqual(bat.get_sound(), 'Screech-Screech-SCREECH', "Enemey:FlyingBat does not make sound")

   # Check if Enemy:FlyingBar makes attack move
   def test_enemy_attacks(self):
      enemy = Enemy()
      self.assertEqual(enemy.attack(), 'YOU BETTER THINK QUICKLY AND DEFEND YOURSELF!!!', "Attack function does not work")


   

   


