class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]
        re = []
        for wi in words:
            re.append("".join(MORSE[ord(w) - ord("a")] for w in wi))

        # print(re)
        return len(set(re))

model = Solution()
model.uniqueMorseRepresentations(words="me")