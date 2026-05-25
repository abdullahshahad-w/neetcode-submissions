class Solution:

    def isAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return False

        freq = [0] * 26

        for i in range(len(str1)):
            freq[ord(str1[i]) - ord('a')] += 1
            freq[ord(str2[i]) - ord('a')] -= 1

        for num in freq:
            if num != 0:
                return False

        return True
         
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        idx = set()

        for i in range(len(strs)):
            if i in idx:
                continue
                
            result = []
            result.append(strs[i])
            idx.add(i)
            for j in range(i + 1, len(strs)):
                if j in idx:
                    continue

                if self.isAnagram(strs[i], strs[j]):
                    result.append(strs[j])
                    idx.add(j)

            ans.append(result)

        return ans










