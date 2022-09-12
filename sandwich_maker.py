import pyinputplus as pyip
cost = 0
print(f'What sandwich would you like?')
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
print(bread)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
print(protein)
cheese = pyip.inputYesNo(prompt = 'Would you like Cheese?')
if cheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
condiments = pyip.inputYesNo(prompt = 'Would you like mayo, mustard, lettuce, or tomato?')
sandwich_count = pyip.inputInt(prompt = 'How many sandwiches would you like?')
if bread == 'wheat':
    cost += .25
if protein =='chicken':
    cost += .75
if cheese == 'cheddar':
    cost += .10
if condiments == 'yes':
    cost += .05
print(f'The total cost is {cost * sandwich_count}')