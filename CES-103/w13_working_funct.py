import math

def compute_area_square(side):
    area= side*side
    return area
def compute_area_rectangle(length,width):
    area=length*width
    return area   
def compute_area_circle(radius):
    area= math.pi*radius**2
    return area

def compute_area(shape, side, width=0):
    area=-1
    #   if shape== 'SQUARE':
    #    area=compute_area_square(side)
    #if shape =='CIRCLE':
    #    area=compute_area_circle(side)
    #if shape == 'RECTANGLE':
    #    area=compute_area_rectangle(side,width)
    return area

user=''

while user.upper()!='QUIT':
    user=input('What is the format of your object? If you want to exit type QUIT!')
    user=user.upper()
    if user=='SQUARE':
        answer=float(input('what is the side of the square?'))
        area_square=compute_area(user,answer)

        print(f'\nThe area of the square is {area_square:.2f} cm^2') 
    if user =='RECTANGLE':
        answer1=float(input('what is the length of the rectangle?'))
        answer2=float(input('what is the width of the rectangle?'))
        area_rectangle= compute_area(user,answer1,answer2)
        print(f'\nThe area of the rectangle is {area_rectangle:.2f}cm^2')

    if user ==  'CIRCLE':
        answer3=float(input('What is the radius of the circle?'))
        area_circle=compute_area(user,answer3)
        print(f'\nThe area of the circle is {area_circle:.2f} cm^2')
print('Okay, bye!')        
