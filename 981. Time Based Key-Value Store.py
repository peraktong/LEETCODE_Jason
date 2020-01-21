import collections
import bisect


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        temp = self.data.get(key, None)
        if not temp:
            return ""
        index = bisect.bisect(temp, (timestamp, chr(127)))
        return temp[index - 1][1] if index else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)