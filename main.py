from managers.insertion_sort import InsertionSort
from managers.quick_sort import QuickSort
import csv
import time

if __name__ == '__main__':
    list_of_sofas_width = []
    list_of_sofas_length = []

    with open('myFile0.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for line in csv_reader:
            list_of_sofas_width.append(line[0])
            list_of_sofas_length.append(line[1])

    print('Sofas sorted by width:')
    time_before_insertion_sort = time.time( )
    InsertionSort.insertion_sort_descending(list_of_sofas_width)
    time_after_insertion_sort = time.time( )
    insertion_sort_time = time_after_insertion_sort - time_before_insertion_sort
    print(list_of_sofas_width)

    print(f'\nTime taken for insertion sorting: {insertion_sort_time} seconds')
    print(f'Amount of swaps : {InsertionSort.number_of_swaps}')
    print(f'Amount of comparisons: {InsertionSort.number_of_comparisons}')
    print('\n')

    print('Sofas sorted by length:')
    time_before_quick_sort = time.time( )
    QuickSort.quick_sort_ascending(list_of_sofas_length, 0, len(list_of_sofas_length) - 1)
    time_after_quick_sort = time.time( )
    quick_sort_time = time_after_quick_sort - time_before_quick_sort
    print(list_of_sofas_length)

    print(f'\nTime taken for quick sorting: {quick_sort_time} seconds')
    print(f'Amount of swaps : {QuickSort.number_of_swaps}')
    print(f'Amount of comparisons: {QuickSort.number_of_comparisons}')

