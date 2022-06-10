from random import randint 

class Dice():
 	"""A Class for the Dice"""
 	def __init__(self, nums_of_side = 6):
 		self.nums_of_side = nums_of_side
 		
 	def roll(self):
 		return randint(1,self.nums_of_side)