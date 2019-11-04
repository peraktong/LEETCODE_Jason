import copy

# trivial:



"""

def dailyTemperatures(T):
    ans = []
    for i in range(0,len(T)-1):

        m1 = T[0]
        T_temp = T[1:]
        T = T[1:]

        if m1 >= max(T_temp):
            ans.append(0)
        else:
            day = 1
            while len(T_temp) > 0:
                if T_temp[0] > m1:
                    break
                else:
                    T_temp.pop(0)
                    day += 1
            ans.append(day)

    ans.append(0)

    print(ans)
    return ans



"""
"""


def dailyTemperatures(T):
    ans = [0] * len(T)
    stack = []  # indexes from hottest to coldest


    for i in range(len(T) - 1, -1, -1):
        # we only consider T[i]<stack, so we drop stack that T[stack]<=T[i]

        while stack and T[i] >= T[stack[-1]]:
            stack.pop()

        ## Here stack are indexes where T[i]<T[stack],
        # and we need the biggest T[stack], which is T[stack[-1]]

        if stack:

            ans[i] = stack[-1] - i
        stack.append(i)
    return ans


"""
def dailyTemperatures(T):
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        # now T[stack]>=t
        stack.append(i)

    print(ans)

    return ans





T=[73, 74, 75, 71, 69, 72, 76, 73]
# Here lambda i: i[1] simply sorts by the second tuple value, i.e. your former value.
l = sorted(enumerate(T), key=lambda i: i[1])
#print(l)
l = [m[0] for m in l]
#print(l)

# for dictionary:
#list(newdict.keys())


dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73])