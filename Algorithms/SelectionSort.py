def selection_sort(arr):
    """Returns the array arr sorted using the selection sort algorithm

    >>> import random
    >>> unordered = [i for i in range(5)]
    >>> random.shuffle(unordered)
    >>> selection_sort(unordered)
    [0, 1, 2, 3, 4]
    """
    if len(arr) <= 1: return arr

    smallest = min(arr)
    del arr[arr.index(smallest)]

    return [smallest] + selection_sort(arr)



if __name__ == "__main__":
    import random

    unordered = [i for i in range(500)]
    random.shuffle(unordered)
    sort = selection_sort(unordered)

    print(sort)
