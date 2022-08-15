from color_dice import ColorDice

red_dice = ColorDice(color='赤')
blue_dice = ColorDice(color='青')
red_dice.roll()
blue_dice.roll()
print(f'{red_dice.color}色のサイコロは: {red_dice.number}')
print(f'{blue_dice.color}色のサイコロは: {blue_dice.number}')
