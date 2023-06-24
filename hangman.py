

import random

# #stages = ['''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']


word_list = ["ardvark", "baboon", "camel"]

# TODO1 - Randomly choose a word from the word list and assign it to a variable called choosen_word.


choosen_word = random.choice(word_list)


# Testing code
print(f"Your choosen word is {choosen_word}")

#TODO2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make a guess lowercase.

#TODO 4 - Create an empty list called display 
# for each letter in the chosen word.
# So if the choosen word was "apple" display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess

display = []
# for letter in range(len(choosen_word)):

word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"
print(display)
    
    
 # todo 8 - Use a while loopo to let the user guess again the loop should only stop once the user ha guessed all the letters in the chosen_word and display has no more blanks. Then you can tell the user they have won    
# todo 9 - Create a variable called lives to keep the track of lives that the user is left with 
# Set lives = 6

lives = 6

end_of_game =  False

while not end_of_game:


    guess = input("Guess a letter ").lower()

    #TODO 3 - Check if the letter the user guessed is one of the letter in choosen word.

    #TODO 5 - Loop thoeugh each position in the choosen_word 
    # if the letter matches with the position then reveal that letter in the display at the position e.g if the user guessed P from apple 
    # ["_", "P", "P", "_", "_"]


    for position in range(word_length):
        letter = choosen_word[position]
        #print(f"Current Position: {position}\n Current Letter: {letter}\n Guessed Letter: {guess}")
        if letter == guess:
            display [position] = letter
            
    # TODO 6 - Print display and you should see the guessed letter current position and every other letter replaced with "_"  
# todo 10 -if the guess is not in the choosen word, then reduce the life by 1 

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Loose:( ")
# if live goes down to 0 then the game should stop and it should print "You loose"

    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You Win!!! ")
        
        
#print(stages[lives])     
        
        
        
