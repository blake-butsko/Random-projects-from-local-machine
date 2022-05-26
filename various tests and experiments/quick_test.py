# For x amount of people how much will the total bill cost if everyone orders a 14 dollar sandwich and 53% of them order 5 dollar fires
# 53% random and with taking percent of x and come up with another way
import random
# dog = 35
# b = 0
# for x in range(dog):
#     b += 1
# print(b)
# print(random.random())

# def coin_flip(number_of_coins):
#     heads,tails = 0,0
#     for x in range(number_of_coins):
#         b = random.random()
#         if b > 0.5: heads += 1
#         else: tails += 1
#     average_heads = round(heads / (heads+tails), 4)
#     average_tails = round(tails / (heads+tails), 4)
#     return f'Heads: {heads}\nTails: {tails}\n' f'Average Heads: {average_heads}%     Average Tails: {average_tails}%'


# print(coin_flip(200000))

# def seaside(number_of_customers, chance_of_fries = 0.53):
#     total = 0
#     for x in range(number_of_customers):
#         if random.random() <= chance_of_fries: total += 19
#         else: total += 14
#     return f'${total} for {number_of_customers} people'

# print(seaside(355))

# integral = 0
# for x in range(5,15+1):
#     x = x*1/100
#     # print(x)
#     integral += ((9*10^9)*(5*10^-9))/(x^2)
# print(integral)

# for x in range(0.05,0.015)

# when will the upgrade be worth it/ paid off
"""
for a dark elixir dril (level 1 -> level 2) inital_rate = 20, upgradge_rate =30, upgrade_time = 12hr
check notebook for what I've written out thus far - I feel like I used that wrong 
"""
# def upgrade_worth(inital_rate, upgrade_rate, upgrade_time):
#     if upgrade_rate - inital_rate <= 0: return('upgrade rate isn\'t increased and therefore won\'t catch up')

# inital = 10
# upgrade = 20
# sum = 0
# def testing_test(rate, days = 7)
#     for x in range(7):
#         rate * 24


# name = input('what is your name: ')
# print(int(name)+2)

import math
#goes through all the possible r values
def num_of_permutations_given_n(n): 
    sum = 0
    for r in range(n+1):
        sum += (math.factorial(n))/(math.factorial(n-r))
        print(sum)
    print(sum)


# num_of_permutations_given_n(7)

def num_of_permutations_given_n_and_r(n,r): 
    print( (math.factorial(n))/(math.factorial(n-r)) )

# num_of_permutations_given_n_and_r(5,3)


bonk = [1,2,3,4,5]
def r_is_three_find_how_many_permutations(n,set_involved):
    n = n
    num = []
    b = 0
    for i in range(n):
        # num[b][0].append(set_involved[i]) 
        for j in range(i+1,n):
            # num[b][1] = set_involved[j]
            for k in range(j+1,n):
                num.append([set_involved[i], set_involved[j], set_involved[k]])
                # num[b][2] = set_involved[k]
                b+=1
    print(num )


r_is_three_find_how_many_permutations(5,bonk)



# stonk = [[0,1],[0]]
# stonk.append([2])
# print(stonk)