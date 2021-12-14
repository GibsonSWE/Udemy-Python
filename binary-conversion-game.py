import random
from replit import clear
print("Welcome to the 8-bit Binary conversion practice game!")
print("Each correct answer awards 1 point.")

loop = True
score = 0
while loop == True:
	int_value = random.randint(0, 256)
	#int_value = 128 #Test value
	binary_value = format(int_value, '08b')
	print("\n____________________________________________________")
	answer = int(input(f"Convert {binary_value} to decimal:\n"))

	if answer == int_value:
		print("Correct! Good job!")
		score += 1
	else:
		print(f"Wrong! The correct answer is {int_value}.")

	again = input('Do you want to try again? Type "y" or "n":  ').lower()
	if again == "n" or again == "no":
		loop = False
	clear()
	
print("\n____________________________________________________")
print(f"\n\nThanks for using the 8-bit Binary conversion practice game! \nYou got {score} points.")
