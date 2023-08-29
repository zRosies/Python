def wind_function(temperature):
    for mph in range (5,61,5):
        v= mph
        wind_chill = 35.74 + 0.6215 * temperature - 35.75*(v**0.16) + 0.4275*temperature*(v**0.16)
        print(f'At the temperature of {temperature:.1f}F, and wind speed {v} mph, the windchill is {wind_chill:.2f}')
 
temperature=float(input('What is the temperature?'))

celsius=input('Fahrenheit or Celsius (F/C)?')
if celsius.upper() == 'C':
   temperature= (temperature*9/5) + 32
else:
    celsius
wind_function(temperature)
 
      


