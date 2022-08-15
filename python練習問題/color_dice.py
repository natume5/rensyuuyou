from dice import Dice

class ColorDice(Dice):
	def __init__(self, number=1, color='白'):
		super().__init__(number=number)
		self.__color = color

	@property
	def color(self):
		return self.__color
