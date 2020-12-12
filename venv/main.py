
import re


def fantz(binary_number, number):
    new_list = ['1']
    min_count = 0

    for i in range(len(binary_number)):
        if len(new_list[i]) >= len(binary_number):
            break
        new_list.append(bin(number ** (i + 1))[2:])
    new_list.reverse()

    for i in new_list:
        result_number, count = re.subn(i, '', binary_number)
        binary_number = result_number
        min_count += count
    if len(binary_number) != 0:
        return -1
    return min_count



