class InsertionSort:
    number_of_comparisons = 0
    number_of_swaps = 0

    @staticmethod
    def insertion_sort_descending(arr):
        InsertionSort.number_of_swaps = 0
        InsertionSort.number_of_comparisons = 0
        for index_of_element in range(1, len(arr)):
            element = arr[index_of_element]
            index_of_another_element = index_of_element - 1
            while index_of_another_element >= 0 and element > arr[index_of_another_element]:
                InsertionSort.number_of_comparisons += 2
                arr[index_of_another_element + 1] = arr[index_of_another_element]
                index_of_another_element -= 1
                InsertionSort.number_of_swaps += 1
            arr[index_of_another_element + 1] = element





