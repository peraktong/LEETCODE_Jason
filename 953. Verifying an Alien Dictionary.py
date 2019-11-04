words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"

def check_order(words,order):
    order_index = {c:i for i,c in enumerate(order)}
    for i in range(0,len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        # find the first different between word1 and word2
        for k in range(min(len(word1),len(word2))):
            if word1[k]!=word2[k]:
                if order_index[word1[k]]>order_index[word2[k]]:
                    return False
                break
        else:
            # perform this only if there is no break executed in the previous step
            if len(word1)>len(word2):
                return False
    return True

# print(check_order(words=words,order=order))
# faster way:
def isAlienSorted(words, order):
    m = {c: i for i, c in enumerate(order)}
    words = [[m[c] for c in w] for w in words]
    return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

def fast(words, order):
    order_index = {c:i for i,c in enumerate(order)}
    words = [[order_index[c] for c in w] for w in words]
    return all(w1<w2 for w1,w2 in zip(words,words[1:]))

print(fast(words=words,order=order))




