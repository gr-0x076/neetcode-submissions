class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 2:
            return n
        L = [0]*n

        L[0] = 1
        L[1] = 2


        for i in range(2, n):
            L[i] = L[i-1] + L[i-2]

        return L[-1]