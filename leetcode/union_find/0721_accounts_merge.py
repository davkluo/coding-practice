from testing import compare_lists

class Solution:
    def accounts_merge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
        Description:
        Given a list of accounts where accounts[i][0] is a name and the rest of
        the elements are emails representing the same account, merge the
        accounts and return them. We can merge accounts that share at least one
        email. Emails should be in sorted order; the accounts can be in any
        order.

        Example:
        accounts_merge([
            ["John", "johnsmith@mail.com", "john00@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"]
        ]) == [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]
        ]
        """

        roots = {}
        rank = {}
        emails_to_account = {}

        def find(email: str) -> str:
            if roots[email] != email:
                roots[email] = find(roots[email]) # path compression
            return roots[email]
        
        def union(email_1: str, email_2: str) -> None:
            root_1, root_2 = find(email_1), find(email_2)

            if root_1 == root_2:
                return
            
            if rank[root_1] < rank[root_2]:
                root_1, root_2 = root_2, root_1
            roots[root_2] = root_1

            if rank[root_1] == rank[root_2]:
                rank[root_1] += 1

        for name, *emails in accounts:
            root_email = None

            for email in emails:
                if email not in emails_to_account:
                    emails_to_account[email] = name

                if email not in roots:
                    roots[email] = email
                    rank[email] = 1

                # assigns first email as root
                if root_email is None:
                    root_email = email
                else:
                    union(root_email, email)
        
        merged_emails = {}
        
        for email, root_email in roots.items():
            root = find(root_email) # root may no longer be a root
            if root not in merged_emails:
                merged_emails[root] = []
            merged_emails[root].append(email)

        merged_accounts = []
        for root_email, account_emails in merged_emails.items():
            merged_accounts.append(
                [emails_to_account[root_email], *sorted(account_emails)]
            )
            
        return merged_accounts
    

if __name__ == "__main__":
    s = Solution()

    # Basic merge: two accounts share an email
    assert compare_lists(
        s.accounts_merge([
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"],
        ]),
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"],
        ],
    )

    # Transitive merge across three accounts
    assert compare_lists(
        s.accounts_merge([
            ["John", "a@mail.com", "b@mail.com"],
            ["John", "c@mail.com", "d@mail.com"],
            ["John", "b@mail.com", "c@mail.com"],
        ]),
        [
            ["John", "a@mail.com", "b@mail.com", "c@mail.com", "d@mail.com"],
        ],
    )

    # Same name, no shared emails — should stay separate
    assert compare_lists(
        s.accounts_merge([
            ["John", "a@mail.com"],
            ["John", "b@mail.com"],
        ]),
        [
            ["John", "a@mail.com"],
            ["John", "b@mail.com"],
        ],
    )

    # Single account, single email
    assert compare_lists(
        s.accounts_merge([["Alice", "alice@mail.com"]]),
        [["Alice", "alice@mail.com"]],
    )

    # All accounts merge into one
    assert compare_lists(
        s.accounts_merge([
            ["Dave", "x@mail.com", "y@mail.com"],
            ["Dave", "y@mail.com", "z@mail.com"],
            ["Dave", "z@mail.com", "w@mail.com"],
        ]),
        [
            ["Dave", "w@mail.com", "x@mail.com", "y@mail.com", "z@mail.com"],
        ],
    )

    print("All tests passed.")