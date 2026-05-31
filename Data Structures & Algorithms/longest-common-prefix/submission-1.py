class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
            
        m=min(len(strs[0]), len(strs[1]))
        str = ''
        for i in range(m):
            if strs[0][i] == strs[1][i]:
                str += strs[0][i]
            else:
                break

        for i in range(2, len(strs)):
            m=min(len(str), len(strs[i]))
            strt = ''
            for j in range(m):
                if strs[i][j] == str[j]:
                    strt += str[j]
                else:
                    break
            str = strt

        return str
            

        