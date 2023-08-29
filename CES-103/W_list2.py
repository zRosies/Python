

with open('courses.txt') as course_file:

    for line in course_file:
        part= line.split(',')
        name= part[0]
        grade= float(part[1])
        bonus = grade +3
        print(f'{name} {grade}')
        #clean_line= line.strip()
        #print(line)
    




#colors= 'red, green, blue, yellow'

#color_parts= colors.split('l')

#print(colors)
#print(color_parts)

#name= 'Brother Burthon                   '

#clean_name=name.strip()

#print(f'----{name}----')
#print(f'----{clean_name}----')
