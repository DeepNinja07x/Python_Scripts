def shellSort(array: list):
    """Returns the array printed using the shell sort algorithm
    	>>> import random
    	>>> unordered_list = [i for i in range(10)]
    	>>> random.shuffle(unordered_list)
    	>>> shellSort(unordered_list)
    	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    	"""
    array_size = len(array)
    # Break array in n/2, n/4, n/8 intervals
    interval = array_size // 2
    while interval > 0:
        for middle_position in range(interval, array_size):
            temp = array[middle_position]
            middle_position_number = middle_position
            while middle_position_number >= interval and array[middle_position_number - interval] > temp:
                array[middle_position_number] = array[middle_position_number - interval]
                middle_position_number -= interval
            array[middle_position_number] = temp
        interval = interval // 2
    print(array)

if __name__ == "__main__":
    shellSort([9, 8, 3, 7, 5, 6, 4, 1, 9, 8, 3, 7, 5, 6, 4, 1])
