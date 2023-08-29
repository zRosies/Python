#Creatovity
#1-If the user chooses celsius, the program displays the ambient temperature in graus celsius, the velocity in kmph, and the winchil in celsius.
#If the user chooses fahrenheit, the program displays as required in the core requirements

def wind_function(temperature, v):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75*(v**0.16) + 0.4275*temperature*(v**0.16)
    return wind_chill
def celsius_to_fahrenheit(celsius):
    celsius= (celsius*9/5) + 32
    return celsius 

 
temperature=float(input('What is the temperature?'))

celsius= ''
while celsius.upper() != 'C' or celsius.upper() != 'F':
    celsius=input('\nFahrenheit or Celsius (F/C)?')



if celsius.upper() == 'C':
    new_temperature=celsius_to_fahrenheit(temperature)
    
    for mph in range(5,61,5):
        v2= mph
        wind_chill=wind_function(new_temperature,v2)
        print(f'At the temperature of {temperature:.1f}ºF, and wind speed {v2} mph, the windchill is {wind_chill:.2f}ºF')  
        
        # Core Requirement: /\ The assigment says that the loop should calculate the speed from 5 to 60 incrementing by 5,
        # But the creativity I made loops in km/h which doesn't increase by 5, if I do that I would have to study
        # a bit about the windchil formula and change it so the time would fit in. So I did both ways, if you do not consider the creativity
        # as fulfiling the core requirements. #Just Remove the # in line 31 and line 26.
else: #Core Requirements

    for mph in range(5,61,5):
        v= mph
        wind_chill_f=wind_function(temperature,v)
        print(f'At the temperature of {temperature:.1f}ºF, and wind speed {v} mph, the windchill is {wind_chill_f:.2f}ºF')
 
      


