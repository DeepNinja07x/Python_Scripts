# Python code to count number of matching
# characters in a pair of strings

# count function
def count(str1, str2):
	c, j = 0, 0
	
	# loop executes till length of str1 and
	# stores value of str1 character by character
	# and stores in i at each iteration.
	for i in str1:	
		
		# this will check if character extracted from
		# str1 is present in str2 or not(str2.find(i)
		# return -1 if not found otherwise return the
		# starting occurrence index of that character
		# in str2) and j == str1.find(i) is used to
		# avoid the counting of the duplicate characters
		# present in str1 found in str2
		if str2.find(i)>= 0 and j == str1.find(i):
			c += 1
		j += 1
	print ('No. of matching characters are : ', c)

# Main function
def main():
	str1 ='aabcddekll12@' # first string
	str2 ='bb2211@55k' # second string
	count(str1, str2) # calling count function

# Driver Code
if __name__=="__main__":
	main()
