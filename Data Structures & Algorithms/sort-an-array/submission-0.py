class Solution:
    def merge(self, arr1, arr2):
        result = []

        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1

            else:
                result.append(arr2[j])
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2

        first = self.sortArray(nums[:mid])
        second = self.sortArray(nums[mid:])

        return self.merge(first, second)














