import unittest 

from twominutesahead import Enemy

class TwoMinutesAheadTestCase(unittest.TestCase):

	def test_enemy_instance(self):
		troll = Enemy()
        self.assertIsInstance(troll, Enemy, msg='Enemy is a base class. Use Troll, FlyingBat')


    def test_inherited_instance(self):
    	troll = Troll('Ring-Nosed-Troll', 'ROAAAAR', 2)
    	self.assertIsInstance(troll, Troll, "Object is an instance of the Troll class")


    def test_inherited_instance2(self):
    	bats = FlyingBat('Dino Bat', 'Screech-Screech-SCREECH', 45)
    	self.assertIsInstance(bats, FlyingBat, "Object is an instance of the FlyingBat class")

   	def test_troll_object_roars(self):
   		troll = Troll('')


