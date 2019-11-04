input_array = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class solution():
    def q_email(self,emails):
        # use set to exclude repeat email
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if "+" in local:
                """
                m1,m2 = local.split("+")
                local = m1

                """
                local = local[:local.index("+")]

            seen.add(local.replace(".", "") + "@" + domain)
        return len(seen)

model = solution()
print(model.q_email(emails=input_array))