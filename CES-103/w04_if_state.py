
percentage=float(input('\nWhat is you grade percentage?'))

if percentage >= 90: 
    letter= 'A'
elif percentage >= 80 < 90: 
    letter ='B'
elif percentage >= 70 < 80:
     letter='C'
elif percentage >=60 < 70:
     letter= 'D'
elif percentage < 60: 
    letter ='F'

number = percentage % 10
if number >= 7: 
    sign= '+'
elif number <3: 
    sign= '-'
else: sign= ''

if letter == 'F':
     sign= ''

if percentage >=93: 
    sign =''

print('\nYour grade is {}{}!'.format(letter, sign))

if percentage >= 70: print('\nCongratulations your grade is {}{} and you have passed the course!'.format(letter, sign))
else: print('\nSorry, you grade is {}{} and you did not passed this semester, try again next time!'.format(letter, sign))









