import collections

class Solution(object):
    def judgeCircle(self, moves):
        m = collections.Counter(moves)
        if m["U"]==m["D"] and m["L"]==m["R"]:
            return True

        else:
            return False



model = Solution()
print(model.judgeCircle(moves="UDL"))
