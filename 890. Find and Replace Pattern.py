class Solution(object):
    def findAndReplacePattern(self,words,pattern):
        def match(word):
            ## Two dictionary mapping from words-pattern and vice versa
            m1 = {}
            m2 = {}

            for w, c in zip(word, pattern):
                if w not in m1:
                    m1[w] = c
                if c not in m2:
                    m2[c] = w
                if (m1[w], m2[c]) != (c, w):
                    return False
            return True

        #return [s for s in words if match(s)]

        return list(filter(match,words))

model =Solution()

words=["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(model.findAndReplacePattern(words=words,pattern=pattern))


