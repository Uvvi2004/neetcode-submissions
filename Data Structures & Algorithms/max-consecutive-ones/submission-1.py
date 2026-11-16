class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not nums:
            return 0

        ones = []

        count = 0

        for num in nums:

            if num == 1:
                count += 1
            if num == 0:
                ones.append(count)
                count = 0
            ones.append(count)
        
        return max(ones)