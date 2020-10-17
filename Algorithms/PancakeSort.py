def pancakeFlip(arr, k):
	"""Returns the array arr reverse sorted using the pancake sort algorithm

	>>> pancakeFlip([1, 2, 3, 4], 3)
	[4, 3, 2, 1]
	"""
	return arr[:k + 1][::-1] + arr[k + 1:]

def pancake_sort(arr):
	"""Returns the array arr reverse sorted using the pancake sort algorithm

	>>> import random
	>>> unordered = [i for i in range(5)]
	>>> random.shuffle(unordered)
	>>> pancake_sort(unordered)
	[0, 1, 2, 3, 4]
	"""

	if len(arr) <= 1: return arr

	largest = arr.index(max(arr))

	arr = pancakeFlip(arr, largest)

	arr = pancakeFlip(arr, len(arr) - 1)

	return pancake_sort(arr[:-1]) + [arr[-1]] 
