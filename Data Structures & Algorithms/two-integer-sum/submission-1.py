class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            track[nums[i]] = i

        for j in range(len(nums)):
            if target - nums[j] in track:
                if j != track[target - nums[j]]:
                    return [j,track[target - nums[j]]]

        return []