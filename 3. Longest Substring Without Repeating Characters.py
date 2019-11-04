class Solution():
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        # start means the beginning of the max length array
        for i, value in enumerate(s):


            if value in dicts:
                # This means we find a repeat
                # Here sums means we find a repeated character and move forward
                sums = dicts[value] + 1
                print(i, value,sums,start)
                print(dicts)
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            # Here dict store the location for each value at each step
            dicts[value] = i
        return maxlength

model =Solution()
print(model.lengthOfLongestSubstring(s="abcabcbb"))