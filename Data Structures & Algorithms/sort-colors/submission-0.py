class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(arr, l, h):
            pivot = arr[h]
            i = l - 1

            for j in range(l, h):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]        

            i += 1
            arr[i], arr[h] = arr[h], arr[i]

            return i

        def quickSort(arr, l, h):
            if l < h:
                pivot = partition(arr, l, h)

                quickSort(arr, l, pivot - 1)
                quickSort(arr, pivot + 1, h)

        return quickSort(nums, 0, len(nums) - 1)