class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_h = Counter(s)
        t_h = Counter(t)
        return s_h == t_h