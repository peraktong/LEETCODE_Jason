from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # DFS:
        # We want each account to be only visied once:
        visited_accounts = [False] * len(accounts)
        email_2_accounts = defaultdict(list)
        ans = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_2_accounts[email].append(i)

        # Here i is the index for account:
        def dfs(i, emails):
            # We visit this account in accounts
            if visited_accounts[i]:
                return None
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in email_2_accounts[email]:
                    dfs(neighbor, emails)

        # run it:
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            ni, emails = account[0], set()
            dfs(i, emails)
            ans.append([ni] + sorted(emails))
        return ans

























