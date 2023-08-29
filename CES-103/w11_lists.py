numbers=[]


number=float(input('Enter a list of numbers, type 0 when finished: '))
average=0
total=0
highest=0
lowest=0
lowest>0
positivies=[]
while number != 0:
    numbers.append(number)
    number=float(input('Enter a list of numbers, type 0 when finished: '))


for number in numbers:
    total+= number
    average= total/ len(numbers)
    highest= max(numbers)
    if number > 0 :
        positivies.append(number)   
print('The sum is {:.2f}'.format(total))
print('The average is {:.3f}'.format(average))
print('The highest number is {:.2f}'.format(highest))
print('The lowest positive number is {:.2f}.'.format(min(positivies)))

sorted_list= sorted(numbers)
print(sorted_list)

for number in sorted_list:
    print(number)

