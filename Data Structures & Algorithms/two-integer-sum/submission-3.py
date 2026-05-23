class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i in range(len(nums)):
            idx[nums[i]] = i

        for j in range(len(nums)):
            remain = target - nums[j]

            if remain in idx and idx[remain] != j:
                return [j, idx[remain]]

        return [-1, -1]