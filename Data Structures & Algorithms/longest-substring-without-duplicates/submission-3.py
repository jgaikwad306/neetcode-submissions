class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_map = set()
        left = 0;
        max_val = 0
        res = 0
        for c in range(len(s)):
            while s[c] in s_map:
                s_map.remove(s[left])
                left+=1
            s_map.add(s[c])
            res = max(res, c-left+1)
        return res
