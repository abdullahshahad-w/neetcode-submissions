class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = {}

        for word in strs:
            current_level = trie
            for c in word:
                if c not in current_level:
                    current_level[c] = {}
                current_level = current_level[c]

            current_level["*"] = True

        result = ""

        current_level = trie

        while True:
            keys = list(current_level.keys())

            if len(keys) > 1 or "*" in keys:
                break

            result += keys[0]
            current_level = current_level[keys[0]]

        
        return result
                

