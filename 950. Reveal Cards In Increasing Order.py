import bisect,collections
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card

            if index:
                m1 = index.popleft()
                index.append(m1)
                print(m1)

        return ans

deck = [17,13,11,2,3,5,7]
# deck.remove to remove element
model = Solution()
print(model.deckRevealedIncreasing(deck = deck))
