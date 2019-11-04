class Solution:
    def trap(self, height):

        arr = height

        height, left, right, water = [], 0, 0, 0
        for i in arr:
            left = max(left, i)
            height.append(left)
        height.reverse()
        for n, i in enumerate(reversed(arr)):
            right = max(right, i)
            water += min(height[n], right) - i
        return water

model = Solution()
print(model.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))