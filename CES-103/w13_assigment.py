#Creatvity
#1-If the user chooses celsius, the program displays the ambient temperature in graus celsius, the velocity in kmph, and the winchil in celsius.
#If the user chooses fahrenheit, the program displays as required in the core requirements.

def wind_function(temperature, v):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75*(v**0.16) + 0.4275*temperature*(v**0.16)
    return wind_chill
def celsius_to_fahrenheit(temperature):
    temperature= (temperature*9/5) + 32
    return temperature 

 
temperature=float(input('What is the temperature?'))

celsius= ''
while celsius != 'C' and celsius != 'F':               #Creativity
    celsius=input('\nFahrenheit or Celsius (F/C)?')
    celsius= celsius.upper()

if celsius.upper() == 'C': #Creativity
    new_temperature=celsius_to_fahrenheit(temperature)
    for mph1 in range(5,61,5):
        v2= mph1
        wind_chill_core=wind_function(new_temperature,v2)

        print(f'At the temperature of {new_temperature:.1f}ºF, and wind speed {v2} mph, the windchill is {wind_chill_core:.2f}ºF') #Creativty
    print('\nThe same temperature in celsius and kilometers per hour is: ') 

    for mph2 in range(5,61,5): # Core Requirement
        v3=mph2
        wind_chill=wind_function(new_temperature,v3)
        print(f'At the temperature of {temperature:.1f}ºC, and wind speed {v3*1.609:.2f} kmph, the windchill is {(wind_chill-32)*5/9:.2f}ºC')   
        
else: #Core Requirement

    for mph3 in range(5,61,5):
        v= mph3
        wind_chill_f=wind_function(temperature,v)
        print(f'At the temperature of {temperature:.1f}ºF, and wind speed {v} mph, the windchill is {wind_chill_f:.2f}ºF')
 
      


