# MEET room 2:

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # similar to meet room2: it
        temp = []
        for i, j, k in trips:
            # start+passenger
            temp.append((j, i))
            # stop+passenger
            temp.append((k, -i))
        temp.sort()
        tot = 0
        for i in temp:
            tot += i[1]
            if tot > capacity:
                return False
        return True



