
import random

ccc='yes'
magic= random.randint(1,10)
number=0
counter= 0

while number != magic or ccc.lower()=='yes':
        number=int(input('What is your guess?'))
        counter= counter + 1 
        if magic > number:
            print('Higher')
        elif magic < number:
            print('Lower')   
        elif number == magic:
                ccc=input('\nCongratulations, you have finished the game after {} attempts. Do you want to play again?(YES or NO)'.format(counter))
                while ccc.upper() not in ('YES', 'NO'):
                    ccc=input('Do you want to play again?(YES or NO)')      
print('\nOkay, have a nice day!'.format(counter))
       
    

    






