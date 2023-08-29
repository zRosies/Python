
average_list=[]
user1=''
user=int(input('\nEnter the year of interest: '))
while user1.upper() != 'NO': #Creativity

    user1=input('\nDo you want to know the life expectancy of a specific country?(yes/no)')
    if user1.upper() == 'YES':
        user_country=input('Type the name of the country: ')
        user_country=user_country.capitalize()
        user1='NO'

with open('life-expectancy.csv') as life_expectancy:
    next(life_expectancy)
    largest=0
    lowest= 1000000
    total=0
    country_low=''
    country_larg=''

    low_country=10000
    larg_country= -1
    lag_year= ''
    low_year=''
    for i,  line in enumerate(life_expectancy):

        line_div=line.split(',')
        country=line_div[0] 
        code=line_div[1]
        year=float(line_div[2])
        l_expec= line_div[3]
        l_expec= float(l_expec)
        l_expec2= line_div[3]
        l_expec2= float(l_expec2)
        
        if user == year: 
            total+=l_expec
            average_list.append(country)
            average=total/len(average_list)
            if l_expec > largest:
                largest= l_expec
                country_larg= country
            if l_expec < lowest:
                lowest= l_expec
                country_low= country
                
        elif user_country == country: #Creativity
            if l_expec2 > larg_country:
                larg_country= l_expec
                lag_year= year
                larg_country= float(larg_country)
            if l_expec < low_country:
                low_country= l_expec 
                low_year= year
                low_year= float(low_year)   


    print(f'\nFor the year of {user}:')
    print(f'\nThe average life expectancy across all the countries was {average:.2f}')           
    print(f'The max life expectancy was {country_larg} with {largest:.2f}')
    print(f'The min life expectancy was {country_low} with {lowest:.2f}')


    print(f'\nFor the country of {user_country}')
    print(f'The max life expectancy was {larg_country:.2f} in {lag_year}')
    print(f'The min life expectancy was {low_country:.2f} in {low_year}')

