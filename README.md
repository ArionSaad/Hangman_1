# Hangman

> This project is about creating the classic game Hangman using python code. The main software used was Visual Studio Code to programme the game. 


## Milestone 1

- The first task was to download a template from GitHub which already included some pre-written code.
- The ask_letter method was completed. This method asks the player for a single letter and if they input multiple letters the player is asked once again to input a single letter. The input letter is assigned to a vaiable called "letter". 
- The following is the code written inside the ask_letter method:

  
```python
while self.num_letters >= 1 and self.num_lives >= 1: # a loop that keeps asking the player for a letter until they either run out of chances of completes the word
            letter = input("Guess a letter") # assigns the guessed letter to a variable 
            if len(letter) > 1: # checks if it is a single letter input
                print("Please, enter just one character") # informs the player of their wrongdoing
            elif len(letter) == 1: # valid input is now checked in the mystery word
                pass
            else:
                print('Please, enter just one character')# in case the other conditions are not met 
```

![Screenshot from 2022-03-29 19-06-17](https://user-images.githubusercontent.com/101988764/160676692-4528210e-ace2-4ee3-9adc-5df9a38163b6.png)


## Milestone 2

- The __init__ method is filled in to initialise the class. All the attributes used in the class are set up here. Two messages are also printed. One tells the player the number of unique letters in the word and the other shows a list of blank spaces indicating the word.

```python
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
      
```

- The ask_letter method is also modified to check if the input letter has already been tried and informs the player if they have done so.

```python
elif letter in self.list_letters: # checks if the letter has already been guessed
                print(f"{letter} was already tried") #informs the player of their wrongdoing

```

![Screenshot from 2022-03-29 19-12-48](https://user-images.githubusercontent.com/101988764/160677712-a514be7e-943c-4587-a83a-e5609d78f415.png)


## Milestone 3

- The check_letter method is completed. This checks if the input letter is in the word. If so the game shows where the letter is in the word. If not the game tells the player they are wrong and they lose a life.

```python
letter = letter.lower() # makes the letter lowercase in case the player uses a captial letter as input
        if self.word_as_list.count(letter) == 0: # condition for when the letter is not in the word
            print(f'Sorry, {letter} is not in the word.') # informs the player of their wrongdoing 
            self.num_lives -= 1 # reduces the player's number of chances by 1
            print(f'You have {self.num_lives} lives left.') # informs the player the number of chances left
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
```
- The ask_letter method is modified to call the check_letter method if the player has input a valid letter.

![Screenshot from 2022-03-29 19-33-27](https://user-images.githubusercontent.com/101988764/160681185-40faab5b-ac88-481e-b4f2-456f93c9a007.png)

## Milestone 4

- The win and loss conditons of the game is set up. If the player correctly inputs all the letters in the word the game ends with a congratulations. If the player loses all their lives the game ends with a game over. This is done inside the ask_letter method.

```python
if self.num_letters == 0: # this condition will be met if all the letters have been guessed correctly
            print("Congratulations! You won!") # gives the player a sense of accomplishment  
        elif self.num_lives == 0: # this condition will be met if the player runs out of chances
            print(f"You lost! The word was {self.word}") # gives the player a sense of frustration  
```
- A basic visualisation of the hangman is also set up.

```pytohn
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
```

![Screenshot from 2022-03-29 19-40-22](https://user-images.githubusercontent.com/101988764/160682249-0f25bf59-e14e-4e15-b9c0-15bc04eabbc1.png)

![Screenshot from 2022-03-29 19-41-08](https://user-images.githubusercontent.com/101988764/160682358-e12cce8a-92e0-4374-864a-93687e9d8ef1.png)




## Conclusions

- The project allowed me to learn the basics of writing python code.
- One option to take the project further would be to link to a databse of words to choose from instead of a limited list of words.
- Adding difficulty options to the game would also be beneficial by catogorising the words by levels of complexity and allowing the player to choose which complexity level they want.
- Currently the game takes non-letter inputs like numbers and symbols as a valid input. One way to improve would be to detect what the input character is and prevent numbers and symbols as valid inputs.

