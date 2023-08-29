#I created an input so the user can know the year wuth max and min life expectancy in the whole period.
coun_average_list=[]
average_list=[]
user1=''
largest= 0
lowest= 1000000
total= 0
low_country= 10000
larg_country= -1
total_expec= 0
average_coun= 0

life_expectancy= open('life-expectancy.csv') 
while user1.upper() != 'NO' or aa.upper() != 'NO': #Creativity
        
        user=int(input('\nEnter the year of interest: '))
        user1=input('\nDo you want to know the life expectancy of a specific country?(YES/NO)')
        if user1.upper() == 'YES':
            user_country=input('Type the name of the country: ')
            user1='NO'
            user3=''
        else:
            user_country = ''
            user3='NO'
            next(life_expectancy)
            
            for line in life_expectancy:

                line_div=line.split(',')
                country=line_div[0] 
                code=line_div[1]
                year=int(line_div[2])
                l_expec = line_div[3]
                l_expec = float(l_expec)

                if user_country.upper() == country.upper(): 
                    total_expec += l_expec
                    coun_average_list.append(l_expec) 
                    num_of_l=len(coun_average_list)
                    average_coun = total_expec/num_of_l

                    if l_expec > larg_country:
                        larg_country = l_expec
                        lag_year= int(year)
                    if l_expec < low_country:
                        low_country = l_expec 
                        low_year= int(year)
        if user3=='':                

            print(f'\nFor the country of {user_country}:')
            print(f'\nThe average of life expectancy throughout the years is {average_coun:.2f}')
            print(f'The max life expectancy was {larg_country:.2f} in {lag_year}.')
            print(f'The min life expectancy was {low_country:.2f} in {low_year}.')  

        with open('life-expectancy.csv') as life_expectancy: #CORE Requirements
            next(life_expectancy)
            for line in life_expectancy:
                line_div=line.split(',')
                country2=line_div[0] 
                code=line_div[1]
                year2=int(line_div[2])
                l_expec2= float(line_div[3])

                if user == year2: 
                    total += l_expec2
                    average_list.append(country2)
                    average = total/len(average_list)
                    if l_expec2 > largest:
                        largest = l_expec2
                        country_larg = country2
                    if l_expec2 < lowest:
                        lowest = l_expec2
                        country_low = country2
            print(f'\nFor the year of {user}:')
            print(f'\nThe average life expectancy across all the countries was {average:.2f}.')           
            print(f'The max life expectancy was in {country_larg} with {largest:.2f}.')
            print(f'The min life expectancy was in {country_low} with {lowest:.2f}.')
        aa=input('?')


    

