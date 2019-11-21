import collections
x = [1, 5, 1, 1, 7, 3, 5]

temp = collections.Counter(x)
temp = sorted(temp.items(),key=lambda x:(x[1],-x[0]),reverse=True)
ans = []
for i in temp:

    ans.extend([i[0]]*int(i[1]))
print(ans)

