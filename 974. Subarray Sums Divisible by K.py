class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        ans, temp_sum = 0, 0
        # counting  {RunningSum%K : Frequency_Count}
        array2 = [1] + [0] * K
        for i in range(len(A)):
            temp_sum += A[i]
            ans += array2[temp_sum % K]
            array2[temp_sum % K] += 1
        return ans


