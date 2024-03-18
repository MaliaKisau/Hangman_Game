import os

# Function to clear the terminal
def clear_terminal():
    os.system('cls')
    
import random

# Importing the list of words for the game 
from hangman_words import word_list

# Choosing a random word from the word list
chosen_word = random.choice(word_list)

# Gettin the length of the choosen word
word_length = len(chosen_word)
#Initializing game variables
end_of_game = False
lives = 6

# Importing the hangman logo
from hangman_art import logo
print(logo)

# Creating blanks for the word to be guessed
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    # Asking the player for a guess
    guess = input("Guess a letter:").lower()
    # Clearing the terminal after each guess
    clear_terminal()
    # Checking if the guessed letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

# Checking the guessed letter against the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Handling incorrect guesses
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. Ypu lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    # Displaying the current state of the word
    print(f"{''.join(display)}")
    
    # Checking if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Importing and displaying the hangman stages 
    from hangman_art import stages    
    print(stages[lives])
    
