'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''

import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}

        self.word = random.choice(word_list) # picks a random word from the list of prespecified words
        self.word_as_list = list(self.word) # breaks the string of the chose word into individual letters in a list
        num_letters_tot = len(self.word) # counts the total number of letter in the list
        blanks = "_" # the blank space to be used to fill up the word_guessed list
        self.word_guessed = [] #sets up the definition of the word_guessed as a list
        self.word_guessed.extend(blanks * num_letters_tot) # populates word_guessed with blank spaces according to the total number of letters in the word
        self.num_letters = len(set(self.word)) # number of unique letters
        self.num_lives = num_lives # number of chances the player gets
        self.list_letters = [] # initialises the list of letters the player will guess 
        print(f"The mistery word has {self.num_letters} characters") # gives the player a hint of the number of unique letters in the list
        print(self.word_guessed) # presents the player with the word_guessed list 
        self.draw_man() # visualises the hangman
        pass

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class

        letter = letter.lower() # makes the letter lowercase in case the player uses a captial letter as input
        if self.word_as_list.count(letter) == 0: # condition for when the letter is not in the word
            print(f'Sorry, {letter} is not in the word.') # informs the player of their wrongdoing 
            self.num_lives -= 1 # reduces the player's number of chances by 1
            print(f'You have {self.num_lives} lives left.') # informs the player the number of chances left
            self.draw_man() # visualises the hangman slowly getting hanged
        elif self.word_as_list.count(letter) >= 1: # if the letter is in the word
            print(f'Nice! {letter} is in the word!') # pats the player on the back
            self.num_letters -= 1 # reduces the number of unique letter by 1
            while self.word_as_list.count(letter) > 0: # a loop set up to replace the letter in the word_guessed list
                letter_pos = self.word_as_list.index(letter) # finds the index of the letter in the word_as_list
                self.word_as_list.pop(letter_pos) # removes the letter from word_as_list
                self.word_as_list.insert(letter_pos , "dummy") # places a dummy item in the list to make indexing manageable 
                self.word_guessed.pop(letter_pos) #removes the blank space from the index position of the word_guessed list 
                self.word_guessed.insert(letter_pos , letter) #places the letter into the index position of the word_guessed list
            print(self.word_guessed) # prints the word_guessed list as it currently stands
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
             
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method

        while self.num_letters >= 1 and self.num_lives >= 1: # a loop that keeps asking the player for a letter until they either run out of chances of completes the word
            letter = input("Guess a letter") # assigns the guessed letter to a variable 
            if len(letter) > 1: # checks if it is a single letter input
                print("Please, enter just one character") # informs the player of their wrongdoing
            elif letter in self.list_letters: # checks if the letter has already been guessed
                print(f"{letter} was already tried") #informs the player of their wrongdoing
            elif len(letter) == 1: # valid input is now checked in the mystery word
                self.list_letters.append(letter) #adds the letter to the list of guessed letter
                self.check_letter(letter) # calls the check_letter function
            else:
                print('Please, enter just one character')# in case the other conditions are not met 
        if self.num_letters == 0: # this condition will be met if all the letters have been guessed correctly
            print("Congratulations! You won!") # gives the player a sense of accomplishment  
        elif self.num_lives == 0: # this condition will be met if the player runs out of chances
            print(f"You lost! The word was {self.word}") # gives the player a sense of frustration     
        pass

    def draw_man(self): # this is to visualise the hangman
        h_u = '_________'
        h_s = '| '
        h_l = '|____'
        h_4 = '|       |'
        h_3 = '|       O'
        h_2 = '|      /|\ '
        h_1 = '|       |'
        h_0 = '|      / \ '
        print(h_u)
        if self.num_lives <= 4:
            print(h_4)
        else:
            print(h_s)
        if self.num_lives <=3:
            print(h_3)
        else:
            print(h_s)
        if self.num_lives <= 2:
            print(h_2)
        else: 
            print (h_s)
        if self.num_lives <= 1:
            print(h_1)
        else:
            print(h_s)
        if self.num_lives <= 0:
            print(h_0)
        else:
            print(h_s)
        print(h_l)
        pass

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5) # initialises the game with the list of prespecified words and 5 chances
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}"

    game.ask_letter() # uses the ask letter function
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%