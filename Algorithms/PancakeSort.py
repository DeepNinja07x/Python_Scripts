def pancakeFlip(arr, k):
	"""Returns the array arr reverse sorted using the pancake sort algorithm

	>>> pancakeFlip([1, 2, 3, 4], 3)
	[4, 3, 2, 1]
	"""
	return arr[:k + 1][::-1] + arr[k + 1:]

def reverse_pancake_sort(arr):
	"""Returns the array arr reverse sorted using the pancake sort algorithm

	>>> import random
	>>> unordered = [i for i in range(5)]
	>>> random.shuffle(unordered)
	>>> reverse_pancake_sort(unordered)
	[4, 3, 2, 1, 0]
	"""

	if len(arr) <= 1: return arr

	largest = arr.index(max(arr))

	arr = pancakeFlip(arr, largest)

	arr = pancakeFlip(arr, len(arr) - 1)

	return [arr[-1]] + reverse_pancake_sort(arr[:-1])
