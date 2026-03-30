class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        count = len(strs[0])
        for i in range(count):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result 