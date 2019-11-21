class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        # binary:
        a = bin(a)[2:]
        b = bin(b)[2:]
        temp=0
        ans = ""
        while a or b or temp>0:
            if a[-1]=="0" and b[-1]=="0":
                if temp==0:
                    ans +="0"
                else:
                    ans+="1"
                    temp=0
            elif (a[-1]=="1") ^ (b[-1]=="1"):
                if temp==0:
                    ans +="1"
                else:
                    ans+="0"
            else:
                if temp==0:
                    ans +="0"
                    temp=1
                else:
                    ans+="1"
            a = a[:-1]
            b = b[:-1]
            if not a:
                a = "0"
            if not b:
                b = "0"

        ans = ans[::-1]
        return int(ans,2)
        """

        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)




