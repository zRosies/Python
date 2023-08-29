
import random
#'creavity': random words in a list, and the user can choose to stop playing before finding the secret word.
#ps: The program works in CAPS.

words=['ronaldy'] 

secret_w = (random.choice(words))
hint= '_ '  * len(secret_w)


print('\nWelcome to the word game!')
print('\nPlease, choose a word with the exact numbers of underscores in the hint!')
print('\nIf you do not want to play anymore, just type STOP!')

print(f'\nYour hint is {hint}!')
guess=input('\nWhat is your guess? ')
count=1
guess.lower()  

while guess.lower() != secret_w and guess.lower() !='stop':
        count=count+1   #count the attempts 
        while len(guess) != len(secret_w) and guess.lower()!='stop':

            print('\nThe guess must have the same number of letters as the secret word!')
            guess= input('\nWhat is your guess? ')#loops either if the user types len(word) != secret_w or STOP
        print('\nYour hint is:')    
        for i, letter in enumerate(secret_w): 
            if guess.lower()[i] == letter: 
                letter= letter.upper()    
            elif guess.lower()[i] in secret_w:  
                letter=guess[i].lower()
            else:
                guess[i] != letter
                letter= '_ '           
            print(letter,end='')      
        guess=input('\nWhat is your guess? ') #loop2
        
# Basic// Plural and singular for attempt
if count== 1:
    attempt='attempt'
else:
    attempt='attempts'    
print()

#End
if guess.lower() == secret_w :
    print('\nCongratulations, you have found the secret word! It took you {} {}!'.format(count, attempt))
else: 
    guess.upper()=='STOP'
    print('Okay, see you next time!')
  











# if letter.lower() != guess.lower():
#        letter= '_'
#     print('{}'.format(letter),end='')