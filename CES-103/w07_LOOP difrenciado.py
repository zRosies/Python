
import random


number= random.randint(1,100)
bbb= random.randint(0,100)   
# bbb= Your guess or the number you choose! I just wrote bbb because I am lazy with words.

while number != bbb:
    if number > bbb:
        bbb = bbb + 1
    if number < bbb:
        bbb = bbb -1 
    print('Your number is {}'.format(bbb))
    if number != bbb and number > bbb :
        print('Higher')
    if number != bbb and number < bbb:
        print('Lower')            
print('Congratulations')  