class Solution:
    def plusOne(self,digits):

        # recursive:
        digits[-1]+=1
        i = -1

        while True:
            if digits[i] < 10:
                break
            else:
                digits[i] =0
                i += -1
                if abs(i)==len(digits)+1:
                    digits.insert(0,1)
                else:
                    digits[i] += 1
        return digits





model = Solution()
print(model.plusOne(digits=[9,9,9]))
