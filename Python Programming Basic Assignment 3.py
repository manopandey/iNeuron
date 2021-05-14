#Question 1
# num = 0
# if num > 0:
#     print(str(num)+" is positive")
# elif num < 0:
#     print(str(num)+" is negative")
# else :
#     print(str(num)+" is Zero")

#Question 2
# number = 0
# if number%2 == 1:
#     print(str(number)+" is Odd")
# else :
#     print(str(number)+" is Even")

#Question 3
# year = 3031
# if year%4==0 and year%100 != 0 or year%400==0:
#     print(str(year)+" is a Leap Year")
# else:
#     print(str(year)+" is not a Leap Year") 


#Question 4
# value = 6700417
# is_prime = True
# divisible_by = 0
# for i in range(2,value):
#     if value%i == 0:
#         divisible_by=i
#         is_prime=False
#         break
        
# if is_prime:
#     print(str(value)+ " is a Prime Number")
# else:
#     print(str(value)+ " is not a Prime Number, divisible by "+str(divisible_by))


#Question 5
is_prime = True
for value in range(1,10001):
    for i in range(2,value):
        if value%i == 0:
            is_prime=False
            break
    if value==1: 
        is_prime=False
            
    if is_prime:
        print(str(value)+ " is a Prime Number")
    else:
        pass
    is_prime = True