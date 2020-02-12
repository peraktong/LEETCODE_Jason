import collections


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = collections.Counter()
        for d in cpdomains:
            count, d = d.split()
            count = int(count)
            frags = d.split(".")
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
