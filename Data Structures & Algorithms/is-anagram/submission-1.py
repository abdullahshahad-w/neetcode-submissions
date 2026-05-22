class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1 = {}

        for char in s:
            count1[char] = count1.get(char, 0) + 1

        count2 = {}

        for char in t:
            if char not in count1:
                return False

            else:
                count2[char] = count2.get(char, 0) + 1

        for char in s:
            if count1[char] != count2[char]:
                return False

        return True