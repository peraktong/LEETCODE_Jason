class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        m1 = {}
        m2 = {}
        for i, val in enumerate(s):
            m1[val] = m1.get(val, []) + [i]
        for i, val in enumerate(t):
            m2[val] = m2.get(val, []) + [i]
        return sorted(m1.values()) == sorted(m2.values())

