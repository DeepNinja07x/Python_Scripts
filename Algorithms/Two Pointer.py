def isPairSum(A, N, X):

	for i in range(N):
		for j in range(N):

			if(i == j):
				continue

		
			if (A[i] + A[j] == X):
				return True

			if (A[i] + A[j] > X):
				break

	return 0

arr = [3, 5, 9, 2, 8, 10, 11]
val = 17

print(isPairSum(arr, len(arr), val))


