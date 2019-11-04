input_array = [1,2,3,4]

def productExceptSelf(input_array=input_array):

    ans = []
    right = []
    right_temp=1
    left = []
    left_temp = 1
    for i in range(len(input_array)):
        left_temp = left_temp * input_array[i]
        left.append(left_temp)

    for i in reversed(range(len(input_array))):
        right_temp = right_temp * input_array[i]
        right.append(right_temp)
    right = list(reversed(right))
    ans = [right[1]]
    for i in range(1,len(input_array)-1):
        ans.append(left[i-1]*right[i+1])
    ans.append(left[-2])

    print(ans)
    return ans







print(productExceptSelf(input_array=input_array))

