def minAddToMakeValid(S):
    if len(S) == 0:
        return 0
    else:
        while "()" in S:
            S = S.replace("()", "")

        return len(S)

def minAddToMakeValid_2(S):
    ans = bal = 0
    for symbol in S:
        bal += 1 if symbol == '(' else -1
        # It is guaranteed bal >= -1
        if bal == -1:
            ans += 1
            bal += 1
    return ans + bal

input = "()))(("

print(minAddToMakeValid(S = input))
print(minAddToMakeValid_2(S=input))

