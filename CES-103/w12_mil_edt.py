#1-I created an input so the user can know the max, min, and average life expectancy of a country in the whole period.
coun_average_list=[]
average_list=[]
largest= 0
lowest= 1000000
total= 0
low_country= 10000
larg_country= -1
total_expec= 0
average_coun= 0
user3= False

with open('life-expectancy.csv') as life_expectancy:
    next(life_expectancy) 
   
    user=int(input('\nEnter the year of interest: '))
    user1=input('\nDo you want to know the life expectancy of a specific country?(YES/NO)')

    if user1.upper() == 'YES':
            user_country=input('Type the name of the country: ')
            user3=True
    else:
            user_country = ''   
            
    for line in life_expectancy:
            #Core requirements
            line_div=line.split(',') 
            country=line_div[0] 
            code=line_div[1]
            year=int(line_div[2])
            life_expec = float(line_div[3])
            #Creativity
            country2=line_div[0] 
            code=line_div[1]
            year2=int(line_div[2])
            life_expec2= float(line_div[3])
            # Creativity: Finding the total, average, min, max ...
            if user_country.upper() == country.upper(): 
                total_expec += life_expec
                coun_average_list.append(life_expec) 
                average_coun = total_expec/len(coun_average_list)

                if life_expec > larg_country:
                    larg_country = life_expec
                    lag_year= int(year)
                if life_expec < low_country:
                    low_country = life_expec 
                    low_year= int(year)
            #Core Requirements, average, min, max of a specific country
            if user == year2: 
                total += life_expec2
                average_list.append(country2)
                average = total/len(average_list)

                if life_expec2 > largest:
                    largest = life_expec2
                    country_larg = country2
                if life_expec2 < lowest:
                    lowest = life_expec2
                    country_low = country2
                    
    print(f'\nFor the year of {user}:') #Core Requirements
    print(f'\nThe average life expectancy across all the countries was {average:.2f}.')           
    print(f'The max life expectancy was in {country_larg} with {largest:.2f}.')
    print(f'The min life expectancy was in {country_low} with {lowest:.2f}.')              
    if user3 == True: # Creativity
        print(f'\nFor the country of {user_country.capitalize()}:')
        print(f'\nThe average of life expectancy throughout the years is {average_coun:.2f}')
        print(f'The max life expectancy was {larg_country:.2f} in {lag_year}.')
        print(f'The min life expectancy was {low_country:.2f} in {low_year}.')
 

        
          



    

