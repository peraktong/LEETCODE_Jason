class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        # Here words is the order of the index: And it should be ascending order.
        words = [[order_index[c] for c in w] for w in words]
        return all(w1 < w2 for w1, w2 in zip(words[:-1], words[1:]))

