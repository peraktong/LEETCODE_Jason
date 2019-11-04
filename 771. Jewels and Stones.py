J = "aAx"
S = "aAAbbbb"

class solution():
    def js(self,j,s):
        # return sum(si in j for si in s)
        print(s.count(j))
        print(list(map(s.count,j)))
        return sum(map(s.count,j))

model = solution()
number = model.js(j=J,s=S)
print(number)
