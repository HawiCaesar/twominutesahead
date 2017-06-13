import unittest 

from twominutesahead import Enemy, Troll, FlyingBat

class TwoMinutesAheadTestCase(unittest.TestCase):

   	def test_troll_instance_of_enemy(self):
   		troll = Troll('Fat-Belly-Troll', 'ROAAAAR', 1)
   		self.assertIsInstance(troll, Enemy, msg='The object should be an instance of the `Enemy` class')


   	def test_flying_instance_of_enemy(self):
   		bats = FlyingBat('Horn-Tailed-Bat', 'Screech-Screech-SCREECH', 35)
   		self.assertIsInstance(bats, Enemy, msg='The object should be an instance of the `Enemy` class')


