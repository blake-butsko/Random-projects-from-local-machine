# 09/21/2021 Blake Butsko (happy birthday)

# book: Fundamentals_of_Digital_Logic_with_Veril
# ch.1 questions 1,6,8 ch.3 questions 1,2,3

# 1.1 base 10(decimal) to binary conversion using the method of dividing by 2 and taking the remainder
def base_10_to_binary():
    b = input('enter decimal value ')
    value = int(b)
    bit = ''
    while(value>0):
        bit += str(int(value%2))
        value = int(value/2)
        # print(bit)
        # print(value)

    print('the end result is ',bit[::-1])
    return bit

# base_10_to_binary()
    


# 1.6
def binary_to_base_10():
    binary = input('enter binary value ')
    binary = binary[::-1]
    decimal = 0
    for x in range(len(binary)):
        # print(binary[x],2**x)
        decimal += int(binary[x]) * (2**x)
    print(decimal)
    return decimal

# binary_to_base_10()
# 11111111111111111111111111111100



# 1.8
def minimum_number_of_bits():
    print(len(base_10_to_binary()))

# minimum_number_of_bits()



# Chapter 3 1,2,3


# 3.1
def base_8_to_decimal():
    b = input('insert base 8 value ')
    b = b[::-1]
    decimal = 0
    for x in range(len(b)):
        decimal += int(b[x]) * (8**x)
    print(decimal)

# base_8_to_decimal()

def convert_string_to_list(string):
    li = []
    li[:0] = string
    # print(li)
    return li
# convert_string_to_list('chicken')

def base_16_to_decimal():
    b = input('insert base 16 value ')
    b = b[::-1]
    list_b = convert_string_to_list(b)
    decimal = 0
    for x in range(len(b)):
        if list_b[x] == 'A': list_b[x] = '10'
        elif list_b[x] == 'B': list_b[x] = '11'
        elif list_b[x] == 'C': list_b[x] = '12'
        elif list_b[x] == 'D': list_b[x] = '13'
        elif list_b[x] == 'E': list_b[x] = '14'
        elif list_b[x] == 'F': list_b[x] = '15'
        decimal += int(list_b[x]) * (16**x)
    print(decimal)

# base_16_to_decimal()

# 3.2
def ones_complement_input():
    b = input('insert binary value ')
    c = convert_string_to_list(b)
    a = ''
    for x in range(len(c)):
        if c[x] == '1': c[x] = '0'
        elif c[x] == '0': c[x] = '1'
        a+=c[x]
    print(a)


def ones_complement(binary):
    b = binary
    c = convert_string_to_list(b)
    a = ''
    for x in range(len(c)):
        if c[x] == '1': c[x] = '0'
        elif c[x] == '0': c[x] = '1'
        a+=c[x]
    return(a)

def binary_to_base_10_modified(binary):
    binary = binary[::-1]
    decimal = 0
    for x in range(len(binary)):
        decimal += int(binary[x]) * (2**x)
    #The plus one makes in 2's complement if you don't add one then it's just ones complement
    print(decimal+1)
    return decimal + 1

def ones_complement_to_decimal():
    b = input('insert binary value ')
    if b[0] == '1':
        print('negative')
        b = ones_complement(b[1:])
        # print(b)
    binary_to_base_10_modified(b)

# ones_complement_to_decimal()


# 3.3 

# if negative take the 1's complement then subtract 1 if not convert to decimal



W1 = 3489660928
H1 = 2147483648
W2 = 1
H2 = 4294967295
print(W1-H1)
# print(len("00000001"))
# print(len("FFFFFFFF"))