# def recur(value):
#     if value <= 10:
#         print(value)
#         return value * 2
#     else:
#         print(value)
#         return recur(recur(value / 3))

# print(recur(27))

# def tank(hampster):
#     return hampster * 2
# print(tank(27))

#Factorial two ways

def factorial_1 (num):
    end_val = 1
    for x in range(1,num+1):
        end_val *= x
    return end_val

pop = 1
def factorial_2 (num):
    if num == num :
        pop = 1
    if num > 0:
        pop *= num
        factorial_2(num - 1)
    else: return pop

# print(factorial_2(5))

# print(factorial_1(2))
