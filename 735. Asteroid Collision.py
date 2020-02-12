import collections


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if not asteroids:
            return None
        # use stack:
        ans = []
        for a in asteroids:
            while ans and a < 0 < ans[-1]:
                if ans[-1] < -a:
                    ans.pop()
                    continue
                elif ans[-1] == -a:
                    ans.pop()
                break
            else:
                ans.append(a)
        return ans


