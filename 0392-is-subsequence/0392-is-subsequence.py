class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count_s = len(s)
        count_t = len(t)

        if count_s == 0:
            return True

        if count_s > count_t:
            return False

        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        
        return self.isSubsequence(s, t[1:])