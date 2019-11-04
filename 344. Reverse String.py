class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the string by uisng..
        start = 0
        index_max = len(s)-1
        while start<index_max-start:
            temp = s[start]
            s[start] = s[index_max-start]
            s[index_max-start] = temp
            start+=1