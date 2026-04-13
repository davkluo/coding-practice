# 721 – Accounts Merge

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Union Find
**Link:** https://leetcode.com/problems/accounts-merge/

---

## Problem Summary

Given a list of accounts where each account has a name followed by emails, merge accounts that share at least one email and return the result with emails sorted.

---

## Key Insight

- Emails are globally unique identifiers — names are not. Two accounts belong to the same person if and only if they share at least one email, regardless of name.
- Union-find over emails reduces the problem to grouping connected components. Within each account, union every email with the first email; shared emails across accounts transitively connect the groups.

---

## Approach

1. Initialize a union-find structure over emails, and an `email → name` map.
2. For each account, union all of its emails with the first email in that account. Record the name for any new email.
3. After processing all accounts, iterate over all emails and group them by their `find()` root.
4. For each group, prepend the name (looked up via any email in the group) and sort the emails.

---

## Why This Works

- Union-find correctly captures transitive relationships: if account A shares an email with account B, and account B shares an email with account C, all three merge into one group through chained unions.
- Path compression and union by rank keep `find()` nearly O(1), so the grouping step is efficient.

---

## Edge Cases

- Same name, no shared emails: accounts remain separate
- Single account with one email: returned as-is
- Chain merge: three+ accounts linked transitively through different shared emails

---

## Time & Space Complexity

- Time: O(n · α(n)) where n is total number of emails — α is the inverse Ackermann function from union-find, effectively constant
- Space: O(n) — for the parent/rank maps and email-to-name map

---

## Common Mistakes

- Using stored parent directly instead of calling `find()` when grouping emails — after unions, a node's immediate parent may not be the true root
- Trying to distinguish accounts by name instead of by shared emails — names are not unique identifiers
- Initializing rank to 0 vs 1 doesn't affect correctness, but be consistent with the rank comparison logic

---

## Alternative Solutions

- BFS/DFS on a graph of emails: build an adjacency list where emails in the same account are connected, then find connected components via traversal — O(n) time, same asymptotic complexity but more memory for the adjacency list.
