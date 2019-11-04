class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # one way + stack ?

        ans = [0] * n
        stack = []
        pre = 0
        for log in logs:
            num, ty, time = log.split(":")
            time = int(time)
            num = int(num)
            if ty == "start":

                if stack:
                    # This means the previous task is not finished
                    # We need to add this period to the total period
                    ans[stack[-1]] += time - pre
                stack.append(num)
                pre = time
            else:
                # stop
                ans[stack.pop()] += time - pre + 1
                pre = time + 1
        return ans



