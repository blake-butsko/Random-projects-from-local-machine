# Blake Butsko 07-27-2021

# import numpy as np
# b = []
# for x in range(100):
#      math.append(x)
# # print(b)

# a = np.array(b)
# print(f'shape of a:{a.shape}')

# c = np.reshape(a, (1, 1, 1))
# print(f"Shape of b: {c.shape}")

# print(c)


# a = np.zeros((5,3,2))
# print(a)


# z = np.ndarray([[1,2,3]])
# print(z)


def find_prime(value):
    for x in range(2,(value//2)+1):
        if value%x == 0: print(value,"is not prime", "divisable by", x); return [x, value]
    print(value," is prime")

def find_prime_silent(value):
    for x in range(2,(value//2)+1):
        if value%x == 0: return [x, value]

divisable_values = []

def find_highest_divisable_value(x):
    print(max(divisable_values))

temp = 0
# for x in range(1,100001):
#     temp = find_prime(x)
#     if temp is not None :divisable_values.append(temp)
    
# print(divisable_values)
# print(max(divisable_values)) #313 is the highest up to 100000
# find_highest_divisable_value(divisable_values)


def find_the_highest_prime_divisable():
    divisable_values = []
    temp = 0
    top = int(input("To what number do you want to check "))
    for x in range(1,top+1):
        temp = find_prime_silent(x)
        if temp is not None :divisable_values.append(temp)
    chicken = max(divisable_values)
    print("The highest prime divisable is", chicken[1],"/",chicken[0])

# find_the_highest_prime_divisable()






# 10/05/2021
# either or in python (xor)

# stank = ['dog','cat']

# if ('cat' in stank) != ('dog' in stank):
#     print('yes')
# else:
#     print('no')


# 10-06-21
# gives ASCII bit code for letter


# 10/17/2021
from math import sqrt
from random import randbytes, randint

from cmath import log10
from decimal import Decimal

# def sqrt_guesser():
#     b = input('From which number do you want to have the sqrt taken ')
#     temp = math.sqrt(b)
#     low = temp*0.8
#     high =  temp*1.2
#     guess =random.randint)
#     while 3 == 3:

#         if low >= guess >= high:
#             print('the ending guess is',guess,'/n'+'The actual answer is',temp)
#             return guess


# x = 4
# b = x*0.5
# x*=1.5
# print(math.sqrt(5))



# 10/22/2021 12:42 am
# implement on gambling game too
# two 00 then 36 slots ~~~~~~~~~~~~~ 38

# def martingale_roulette_simulator():
#     starting_money = input()
#     while starting_money > 0:
#         if random.randint(0,36) >= 17: 
#         18/37 chance for either black or red

nums=[3,2,4]
# for x in nums:
#     for y in nums[nums.index(x)+1::]:
#         print(x,y)
# stink =[3,3,3,3]
# print(stink.index(3),stink.index(3,stink.index(3)+1))

coins = [1,0.25,0.1,0.05,0.01]
coins_name = ['dollar', 'quarter', 'dime', 'nickel', 'penny']


def cashiers_algorithm(change_due):
    change_due = Decimal(str(change_due))
    coins_used = 'change:'
    i = 0
    key = False
    while change_due > 0:
        if (change_due - Decimal(str(coins[i]))) > 0:
            print(change_due)
            if change_due == 0.2 :
                coins_used += ' ' + coins_name[i]
                print(coins_used)
                # global key = True
            coins_used += ' ' + coins_name[i]
            change_due -= Decimal(str(coins[i]))
            

        else:
            i += 1
        if key:
            break
    print(coins_used)



# cashiers_algorithm(5)
print(50 % 32)
print((360/8) % 32)
# tank = 0
# while(tank < 5): 
#     if tank > 3:
#         print('lets get out of here')
#         break
#     print('we can take them there\'s only' ,tank,'tanks')
#     tank+=1



#if ekek-coin>0 else coin[i+1]

# coins_used = 'change: '
# coins_used += coins_name[2]
# coins_used += coins_name[3]
# print(coins_used)
