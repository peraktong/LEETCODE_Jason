from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # we want each account to be visted only once:
        visited_accounts = [False] * len(accounts)
        email_2_account = defaultdict(list)
        ans = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_2_account[email].append(i)

        # define: DFS
        # Here the input is the index for the account and set(emails)
        def dfs(i, emails):
            if visited_accounts[i]:
                return None
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neightbor in email_2_account[email]:
                    dfs(neightbor, emails)

        # run DFS
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            ni, emails = account[0], set()
            dfs(i, emails)
            ans.append([ni] + sorted(emails))

        return ans




















