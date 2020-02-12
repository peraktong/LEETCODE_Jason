class Solution(object):
    def getHint(self, secret, guess):
        bull, cow = 0, 0
        s = {}  # secret hashtable
        g = {}  # guess hashtable

        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1

        for k in s:
            if k in g:
                cow += min(s[k], g[k])

        return '{0}A{1}B'.format(bull, cow)