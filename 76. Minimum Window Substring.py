S = "ADOBECODEBANC"
T = "ABC"

def minimum_windows(S,T):
    if set(T)==(set(S)&set(T)):
        min_val = len(S)
        for start in range(len(S)-1):
            stop = start

            while stop < len(S):
                stop += 1
                #print(start, stop, min_val)

                if set(T) == (set(S[start:stop]) & set(T)) and (stop - start) < min_val:
                    min_val = stop - start
                    temp = S[start:stop]

        print(temp)
        return temp

    else:
        print("nothing")
        return ""

ans = minimum_windows(S=S,T=T)
print(ans)

"""
if set("BAC")== (set("ABC"))&(set("ABCD")):
    print("YES")


"""

