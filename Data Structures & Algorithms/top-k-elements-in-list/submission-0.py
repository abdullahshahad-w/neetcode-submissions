class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        count = [[] for _ in range(len(nums) + 1)]

        for key, value in freq_dict.items():
            count[value].append(key)

        result = []

        i = len(count) - 1
        while k > 0:
            for num in count[i]:
                result.append(num)
                k -= 1

            i -= 1

        return result