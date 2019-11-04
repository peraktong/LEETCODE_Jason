
class Solution(object):

    def findContestMatch(self, n):

        # use tuple
        ans = dict()
        team_array = list(range(1, n + 1))
        count=1
        while n > 1:
            self.count = count


            pair_array = []
            [pair_array.append("({},{})".format(team_array[i], team_array[n-i-1])) for i in range(0, n // 2)]
            team_array = pair_array


            # print(team_array)
            ans["%d th round"%count] = team_array
            n = int(n / 2)
            count+=1


        return str(ans["%d th round"%self.count][0])


model = Solution()
print(model.findContestMatch(n=8))
