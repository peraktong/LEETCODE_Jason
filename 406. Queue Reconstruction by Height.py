input_array = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

def reconstruct(input_array):
    # sort from big to small on height, then small to big on num
    input_array.sort(key=lambda x: (-x[0], x[1]))

    output = []
    for p in input_array:
        output.insert(p[1], p)

    return output


print(reconstruct(input_array=input_array))