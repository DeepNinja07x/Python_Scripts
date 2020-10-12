def quick_sort(arr):
    """Returns the array arr sorted using the quick sort algorithm

    >>> import random
    >>> unordered = [i for i in range(5)]
    >>> random.shuffle(unordered)
    >>> quick_sort(unordered)
    [0, 1, 2, 3, 4]
    """
    less = []
    equal = []
    greater = []

    if len(arr) < 1:
        return arr

    pivot = arr[len(arr) // 2]  # pivot at mid point
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            greater.append(num)

    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    import random

    unordered = [i for i in range(5)]
    random.shuffle(unordered)
    sort = quick_sort(unordered)

    print(sort)
