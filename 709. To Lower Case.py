class Solution:
    def toLowerCase(self, str: 'str') -> 'str':
        return str.lower()
"""
class Solution:
    def toLowerCase(self, str):
        
        #type str: str
        #rtype: str
        
        res = ""
        for s in str:
            if ord('A') <= ord(s) <= ord('A')+25:
                res += chr(ord(s)-ord('A')+ord('a'))
            else:
                res += s
        return res

"""