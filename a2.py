#NAME: AMAN REHMAN
#SECTION A
#ROLL NO.: 2017278
import unittest
from tictactoe import game1
from tictactoe import game2
from tictactoe import game3
from tictactoe import validBoard
from tictactoe import takeNaiveMove
from tictactoe import takeStrategicMove


class testpoint(unittest.TestCase):
	def test_game1(self):
	 	self.assertAlmostEqual(game1(10000),0.585,delta=.015)
	 	self.assertAlmostEqual(game1(50000),0.587,delta=.015)
	 	self.assertAlmostEqual(game1(20000),0.585,delta=0.015)

	def test_game2(self):
	 	self.assertAlmostEqual(game2(10000),0.0217,delta=.015)
	 	self.assertAlmostEqual(game2(5000),0.021,delta=.018)
	 	self.assertAlmostEqual(game2(50000),0.0225,delta=.00155)

	def test_game3(self):
	 	self.assertAlmostEqual(game3(10000),0.085,delta=.015)
	 	self.assertAlmostEqual(game3(50000),0.085,delta=.025)
	 	self.assertAlmostEqual(game3(30000),0.0826,delta=.0155)

	def test_takeNaiveMove(self):
	 	self.assertNotEqual(takeNaiveMove(),None)

	def test_takeStrategicMove(self):
	 	self.assertNotEqual(takeStrategicMove(),None)

if __name__=='__main__':
	unittest.main()