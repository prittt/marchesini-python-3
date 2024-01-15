secret_number = 42
num_of_guesses = 1

# Read in user's guess as an integer
user_guess = int(input("Please enter a number:"))

while user_guess != secret_number and num_of_guesses < 5:
	print("Incorrect.")
	user_guess = int(input("Please enter a number:"))
	num_of_guesses += 1

if user_guess == secret_number:
	print("Correct")
else:
	print("Incorrect. Game over.")
