class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        strr = ""
        a = strs[0]
        b = strs[-1]
        for i in range(len(a)):
            if (a[i] != b[i]):
                return strr
            strr += a[i]
        return strr
        