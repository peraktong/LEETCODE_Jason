import collections


def getCounter(i):
    # if i < 10:
    #    return collections.Counter(range(i+1))
    threshold = 10
    counters = [collections.Counter({0: 1})]
    while i >= threshold:
        cur_counter = counters[-1]
        next_counter = collections.Counter()
        for num in cur_counter:
            for leading in range(10):
                next_counter[num + leading] += cur_counter[num]
        counters.append(next_counter)
        threshold *= 10
    threshold //= 10

    res = collections.Counter()
    leading = 0
    i += 1
    while i:
        max_digit = i // threshold
        cur = counters.pop()
        for num in cur:
            for digit in range(max_digit):
                res[leading + digit + num] += cur[num]
        leading += max_digit
        i %= threshold
        threshold //= 10
    return res


def waysToChooseSum(i, j):
    c = getCounter(j) - getCounter(i - 1)
    s = max(c.values())
    return s, list(c.values()).count(s)