def bubble_sort(arr): 
    """Returns the array arr sorted using the bubble sort algorithm

    >>> import random
    >>> unordered = [i for i in range(5)]
    >>> random.shuffle(unordered)
    >>> bubble_sort(unordered)
    [0, 1, 2, 3, 4]
    """
    for i, j in enumerate(arr):
        if i + 1 >= len(arr): continue
        if j > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            return bubble_sort(arr)

    return arr

if __name__ == "__main__":
    import random

    unordered = [i for i in range(5)]
    random.shuffle(unordered)
    sort = bubble_sort(unordered)

    print(sort)
