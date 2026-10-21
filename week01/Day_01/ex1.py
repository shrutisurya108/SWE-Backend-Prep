# Temperature converter
# Temperature converter: read Celsius from input, print Fahrenheit rounded to 1 decimal (F = C * 9/5 + 32).
temp = input("Enter the temperature in celsius: ")
cel = int(temp)
ftemp = cel * 9/5 + 32
print(round(ftemp,1))