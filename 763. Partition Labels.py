def partitionLabels(S):

    dict_last_loc = {c:i for i,c in enumerate(S)}

    j=anchor=0
    ans = []

    for i,c in enumerate(S):

        j = max(j,dict_last_loc[c])
        if i == j:
            print(i,j,anchor,c)
            ans.append(j - anchor + 1)
            # move to next sub-string
            anchor = i + 1

    return ans


S = "ababcbacadefegdehijhklij"

print(partitionLabels(S=S))