# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, T):
    # write your code in Python 3.6
    # convert number array to number
    # edge case two empty: True:
    if not S and not T:
        return True
    if (not S) ^ (not T):
        return False

    # use dual pointers to save space
    # left, right are pointers in S and T
    # curleft and curright are numerical values for numbers in S and T between alphabets
    left = 0
    right = 0
    curleft = 0
    curright = 0
    # check until pointer reaches end of the string and numerical values=0
    while (left < len(S) or curleft != 0) and (right < len(T) or curright != 0):
        if left < len(S) and S[left].isdigit():
            # S is digit
            curleft = int(S[left])
            left += 1
            while left < len(S) and S[left].isdigit():
                curleft = curleft * 10 + int(S[left])
                left += 1
        if right < len(T) and T[right].isdigit():
            # T is digit
            curright = int(T[right])
            right += 1
            while right < len(T) and T[right].isdigit():
                curright = curright * 10 + int(T[right])
                right += 1

        if curleft == 0 and curright == 0:
            # all alphabet
            if S[left].isalpha() and T[right].isalpha() and S[left] != T[right]:
                return False
            left += 1
            right += 1
        else:
            if curleft and curright:
                # all num, num = num-min(num1.num2)
                curleft, curright = curleft - min(curleft, curright), curright - min(curleft, curright)
            elif curleft:
                # T is alphabet but S is num
                right += 1
                curleft -= 1
            elif curright:
                # S is alphabet but T is num
                left += 1
                curright -= 1
    if len(S) == left and len(T) == right and curright == curleft:
        return True

    return False


print(solution(S="12s24d3ee", T="11ss23td5"))



