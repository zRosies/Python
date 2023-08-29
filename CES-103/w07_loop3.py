#import random
#number= 0
#magic_number= random.randint(1,100)
#print('Your magic number is {}'.format(magic_number))


#while number > 6 or number < 6:
#    number=float(input('What is the magic number?'))
#    if number < 6:
#        print('Higher')
#    if number > 6:
#        print('Lower')            
#print('Congratulations')

import random


number= random.randint(1,100)
bbb= 0   

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