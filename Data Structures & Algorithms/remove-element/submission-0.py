class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0

        while i < len(nums):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            else:
                i += 1

        return k