
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]



class Solution(object):
    def anagramMappings(self, A, B):
        D = {x: i for i, x in enumerate(B)}
        print(D)
        return [D[x] for x in A]


model =Solution()
print(model.anagramMappings(A = A,B=B))

