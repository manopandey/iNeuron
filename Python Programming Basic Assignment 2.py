#Question 1
distance_km = 12
distance_miles = distance_km*0.6214
print(distance_miles)

#Question 2
temp_celsius = 57
temp_fahrenheit = temp_celsius*1.8+32
print(temp_fahrenheit)

#Question 3
import calendar
calendar = calendar.month(2021,5)
print(calendar)

#Question 4
import math
a = 2
b = 5
c = -3

try:
    quad1 = (-(b)+math.sqrt(b**2-4*a*c))/(2*a)
    quad2 = (-(b)-math.sqrt(b**2-4*a*c))/(2*a)
    print(quad1,quad2)
except:
    print("No Real Number Solution")


#Question 5
a = 156
b = 196
a,b = b,a
print(a,b)