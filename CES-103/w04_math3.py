square=int(input('What is the length of the side of the square in centimenters?'))
area= square * square
areax = area/10000
print(f'The area of the square is {area} cm^2 or {areax} m^2 ')

print()

rectangle= int(input('What is the length of the side of the rectangle in centimeters?'))
rectangle2= int(input('What is the width of the side of the rectangle in centimeters?'))
area2 = rectangle * rectangle2
areay= area2/10000
print(f'\nThe area of the rectangle is {area2} cm^2 or {areay} m^2')

from math import pi


print()

Circle= int(input('What is the radius of the circle?'))
area3= Circle * Circle * pi
areap= area3/10000
print(f'The area of the circle is {area3} cm^2 or {areap} m^2')