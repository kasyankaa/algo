import re


def fantz(binary_number, number):

    exponentiation_list = ['1']
    min_count = 0
    if len(binary_number)>=100:
        print("binary number is too long")
        quit()
    if number>=100:
        print("number is too big")

    for i in range(len(binary_number)):
        if len(exponentiation_list[i]) >= len(binary_number):
            break
        exponentiation_list.append(bin(number ** (i))[2:])#adding number in different ^ to  list
    exponentiation_list.reverse()
    # print(exponentiation_list)

    for i in exponentiation_list:
        result_number, count = re.subn(i,'', binary_number)
        print(count)
        binary_number = result_number
        min_count += count
        if binary_number==1:
            break

    return min_count



