#Question 1
factorial_num = 7
factorial_output=1
for i in range(factorial_num):
    factorial_output*=i+1
print(factorial_output)

#Question 2
multiplication_table=12
print("Multiplication Table for "+str(multiplication_table))
for i in range(12):
    print(str(i+1)+" X "+str(multiplication_table)+" = "+str(multiplication_table*(i+1)))

#Question 3
fibonacchi_range=20
fibonacchi_list=[0,1]
for i in range(fibonacchi_range-2):
    fibonacchi_list.append(fibonacchi_list[i]+fibonacchi_list[i+1])
print(fibonacchi_list)

#Question 4
sarm_list=[153, 370, 371, 407,1634, 8208, 9474]
for sarm_num in sarm_list:
    sarm_calculate = sum([int(d)**len(str(sarm_num)) for d in str(sarm_num)])
    if sarm_num==sarm_calculate:
        print(str(sarm_num)+ " is a Stongarm Number")
    else:
        print(str(sarm_num)+ " is not a Stongarm Number")


#Question 5
sarm_range=5
for sarm_num in range(sarm_range):
    sarm_calculate = sum([int(d)**len(str(sarm_num)) for d in str(sarm_num)])
    if sarm_num==sarm_calculate:
        print(str(sarm_num)+ " is a Stongarm Number")
    else:
        print(str(sarm_num)+ " is not a Stongarm Number")

#Question 6
first_num = 1
last_num = 100
sum=0
for i in range(first_num,last_num+1):
    sum+=i
print(sum)