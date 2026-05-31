class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            new = ''
            for i in range(min(len(prefix), len(s))):
                if prefix[i] == s[i]:
                    new += prefix[i]
                else:
                    break
            prefix = new
            if not prefix:
                break
        return prefix