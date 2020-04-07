class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # use stack to store [s2,s3] and s2>s3, find max s3 and find s1<s3

        data = [float("-inf")]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < data[-1]:
                return True
            else:
                while data and nums[i] > data[-1]:
                    v = data.pop()
                # v<nums[i]  [i,v]=[s2,s3]
                data.append(nums[i])
                data.append(v)
        return False


