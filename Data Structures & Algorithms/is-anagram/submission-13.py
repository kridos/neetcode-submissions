from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency_s = Counter(s)
        frequency_t = Counter(t)

        if frequency_s != frequency_t:
            return False

        return True