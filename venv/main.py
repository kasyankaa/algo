import re


def fantz(binary_number, number):
    exponentiation_list = ['1']
    min_count = 0
    if len(binary_number) >= max_num:
        print("binary number is too long")
        quit( )
    if number >= max_num:
        print("number is too big")

    for i in range(len(binary_number)):
        if len(exponentiation_list[i]) >= len(binary_number):
            break
        exponentiation_list.append(bin(number ** (i+1))[2:])  # adding number in different ^ to  list
    exponentiation_list.reverse( )
    print(exponentiation_list)

    for i in exponentiation_list:
        result_number, count = re.subn(i, '', binary_number)
        binary_number = result_number
        min_count += count
    if len(binary_number) != 0:
        print("wrong binary number given")
        quit()
    return min_count



