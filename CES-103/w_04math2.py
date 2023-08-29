from math import pi


square=int(input('Choose a number for a length:'))
area = square *square
area2 = square * square * pi
volume = square **3
volume2 = 4/3 * pi * square **3 



print(f'The area of the square is this length is {area} cm^2')
print(f'The area of the circle is this length {area2} cm^2')
print(f'The volume of a cube with this lenght is {volume} cm^3')
print(f'The volume of a sphere with this lenght is {volume2} cm^3')