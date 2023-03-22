import random

computer = ['Rock', 'Paper', 'Scissors']
comp_answers = random.choice(computer)

userInput = input('Rock, Paper or Scissors: ').lower()

# Give the answer right after the input
print(f'Computer: {comp_answers}')

# User 'rock' options
if userInput == 'rock' and comp_answers == 'Rock':
    print('\nTie!')

elif userInput == 'rock' and comp_answers == 'Paper':
    print('\nYou lost!')

elif userInput == 'rock' and comp_answers == 'Scissors':
    print('\nYou won!')

# User 'paper' options
elif userInput == 'paper' and comp_answers == 'Rock':
    print('\nYou won!')

elif userInput == 'paper' and comp_answers == 'Paper':
    print('\nTie!')

elif userInput == 'paper' and comp_answers == 'Scissors':
    print('\nYou lost!')

# User 'scissors' options
elif userInput == 'scissors' and comp_answers == 'Rock':
    print('\nYou lost!')

elif userInput == 'scissors' and comp_answers == 'Paper':
    print('\nYou won!')

elif userInput == 'scissors' and comp_answers == 'Scissors':
    print('\nTie!')

else:
    print('\nInvalid Input!')