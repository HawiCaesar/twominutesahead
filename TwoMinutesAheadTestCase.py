import unittest 

from twominutesahead import Enemy, Troll, FlyingBat

class TwoMinutesAheadTestCase(unittest.TestCase):

	#Check if Troll and Flying bat are instances of Enemy
   	def test_troll_instance_of_enemy(self):
   		troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1)
   		self.assertIsInstance(troll, Enemy, msg='The object should be an instance of the `Enemy` class')


   	def test_flying_instance_of_enemy(self):
   		bats = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 35)
   		self.assertIsInstance(bats, Enemy, msg='The object should be an instance of the `Enemy` class')

   	def test_enemy_objects_is_zero(self):
   		troll = Troll('Short-Snout-Troll', 'ROAAAAR', 0)
		self.assertEqual(troll.attack(), "You are a lucky today they are not coming for you!", "No enemies for the moment")


