import math


def compute_area_rectangle(length,width):
    area_rec=length * width
    return  area_rec
    
def compute_area_square(number):
    area_square= number * number
    return area_square
   
    
def comput_area_circle(radius):
    return radius*radius * math.pi 

def compute_area(user, value1, value2):
    area=-1
    if user == 'square':
        return compute_area_square(value1)
    if user == 'circle':
        return comput_area_circle(value2)
    return user    
            


user=''
while user.lower() != 'no':
    user=input('What is the shape of the object?')

    if user.lower() == 'square':

        square=input('\nWhat is the length of the square ')
        square=float(square)
        area_square=compute_area(user,square, '')
        print(f'\nThe area of the square is {area_square:.2f} cm2')

    if user.lower() =='rectangle':
        
        length=float(input('\nWhat is the length of the rectangle?'))
        width=float(input('What is the width of the rectangle?'))
        area_rectangle=compute_area_rectangle(length,width)
        print(f'\nThe area of the rectangle is {area_rectangle:.2f} cm^2')

    if user.lower()== 'circle':
        radius=float(input('\nWhat is the radius of the circle?'))
        area_circle=compute_area(user,0,radius) 
        print(f'\nThe area of the circle is {area_circle:.2f} cm^2')
    user=input('Do you want to know another shape?(YES/NO)')      