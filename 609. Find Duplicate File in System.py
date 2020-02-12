import collections


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        data = collections.defaultdict(list)
        for l in paths:
            temp = l.split()
            for t in temp[1:]:
                name, b, content = t.partition("(")
                data[content[:-1]].append(temp[0] + '/' + name)

        return [x for x in data.values() if len(x) > 1]


