import random
import hangman_art as hart # this file stores the logo and hangman art 😜 
import hangman_word_list as wl # this file stores the word list 😜 


word_choice = random.choice(wl.word_list) # randomly selects the word from word list.

tracklist = [] 

lives=6 

win=True

for i in range(0,len(word_choice)):
    tracklist.append('_') # filling the list with empty spaces,

print(hart.logo) #shows logo of hangman

while (tracklist.count("_") != 0): # loops untils there is no blank spaces left in tracklist

    guess_letter = input("Guess a letter 👉: ")[0].lower() # inputs the guess letter, even though input funtion inputs a string, but we need a letter so '[0]' gets the first index, for edge cases, and the input string is converted to lowercase.

    if guess_letter in word_choice: # checks if the guess letter is present in the word choice,

        for i in range(0,len(word_choice)):
            # if yes updates the the track list
            if(guess_letter == word_choice[i]):
                tracklist[i] = guess_letter
    else:
        #if no we loose a life and if the life count is less than 0 we loose and exits the game
        print(hart.stages[lives])
        lives -=1

        if(lives < 0):
            win=False
            break
        else:
            print(f"You have only {lives+1} health points more 😬 !!!") # lives+1 is used because of index starts from 0, we cannot continue in the game if we have 0 lives 😬.

    output_string=' '.join(tracklist) #converts the list to a string (for better view), ' '.join -> adds spaces in between letters of the output string.

    print(f"Correct guesses 😇  : {output_string} \n")#here is the output string

if win:
    print("That's correct, You win 🤩 🥳 😎!!!")
else:
    print(f"You loose! 😵 👻 💀 ,The word was {word_choice}")
