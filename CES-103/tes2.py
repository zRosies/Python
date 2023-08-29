ride= False
age=int(input('\nWhat is the age of the first rider?'))
#strech2\/ (the variable age turns '18' answer is 'yes'!)
if age>=12 and age < 18:
    passport=input('\nDo you have a golden passport?')
    if passport.lower()=='yes':
        age=18
height=float(input('\nWhat is the height of the first rider?'))           
rider2=input('\nDo you have a second driver?(YES or NO?)')

if rider2.capitalize() =='Yes':
    age_2=int(input('\nWhat is the age of the second rider?'))
    #strech2\/(the variable age_2 turns '18' if answer is 'yes'!)
    if age_2 >=12 and age_2 < 18:
        passport2=input('\nDo you have a golden passport?')
        if passport2.lower()=='yes':
            age_2=18
    height_2= float(input('\nWhat is the height of the second rider?'))
    
    if height < 36 or height_2 < 36:
        ride=False
    else:
        if age >=18 or age_2 >=18:
            ride=True
            #Strech 1\/(for ages == 12 go together)
        elif age < 18 and age_2 < 18:
            if age >= 12 and age_2>=12:
                if height >=52 and height_2 >=52:
                    ride=True
            #Strech 3\/ (for ages 16 and 14 go together)    
        elif age < 18 and age_2 < 18:
            if age >= 16 and age_2 >=14:
                ride=True
            elif age_2 >=16 and age >=14:
                ride=True    
        else: ride=False
else:
    if age >= 18 and height >= 62:
        ride=True                          
    else:
        ride=False    
       
if ride:
    print('\nCongratulations, you may ride! Have fun :D!')
else: 
    print('\nSorry, you cannot ride!')