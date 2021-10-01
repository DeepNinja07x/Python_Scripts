class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        s = set(A)
        if len(s) == len(A):
            return -1
        for i in A:
            if A.count(i) > 1:
                return i
        else:
            return -1
