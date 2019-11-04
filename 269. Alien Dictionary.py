import collections


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # we can use queue?
        less = []
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for w in range(min(len(w1), len(w2))):
                a = w1[w]
                b = w2[w]
                if a != b:
                    less.append(a + b)
                    break
        chars = set("".join(words))
        order = []
        while less:
            # pair[1] is the second element in the "ab" element
            free = chars - {pair[1] for pair in less}
            if not free:
                return ""
            chars = chars - free
            less = [pair for pair in less if free.isdisjoint(pair)]
            order.extend(free)

        return "".join(order + list(chars))


