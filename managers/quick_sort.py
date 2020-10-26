class QuickSort:
    number_of_comparisons = 0
    number_of_swaps = 0
    @staticmethod
    def partition(arr, low, high):
        smaller_index = (low - 1)
        pivot = arr[high]  # pivot
        for current_element in range(low, high):
            if arr[current_element] <= pivot:
                QuickSort.number_of_comparisons+=1
                smaller_index = smaller_index + 1
                arr[smaller_index], arr[current_element] = arr[current_element], arr[smaller_index]
                QuickSort.number_of_swaps+=2
        arr[smaller_index + 1], arr[high] = arr[high], arr[smaller_index + 1]
        QuickSort.number_of_swaps += 2
        return smaller_index + 1

    @staticmethod
    def quick_sort_ascending(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            QuickSort.number_of_comparisons += 1
            pi = QuickSort.partition(arr, low, high)
            QuickSort.quick_sort_ascending(arr, low, pi - 1)
            QuickSort.quick_sort_ascending(arr, pi + 1, high)



















