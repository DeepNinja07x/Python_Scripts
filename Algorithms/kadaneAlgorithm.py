# Kadane's algorithm takes a non-empty array of integers and returns the 
# maximum sum that can be obtained by summing up the subarrays of the main 
# input array

def kadanesAlgorithm(array):
	maxEnding = array[0]
    currMaximum = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEnding = max(num, maxEnding + num)
        currMaximum = max(currMaximum, maxEnding)
    return currMaximum
