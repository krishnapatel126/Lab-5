fahrenheit_temps = [90, 87, 76, 25, 35]
print("Temperatures in Fahrenheit:", fahrenheit_temps)

celsius_temps = [(temp - 32) * 5/9 for temp in fahrenheit_temps]
print("Temperatures in Celsius:", celsius_temps)
