# 134 – Gas Station

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Greedy
**Link:** https://leetcode.com/problems/gas-station/

---

## Problem Summary

Given arrays `gas` and `cost`, find the starting gas station index from which you can complete a circular circuit, or return -1 if none exists.

---

## Key Insight

- If total gas >= total cost, a valid starting station is always guaranteed to exist. The ordering of stations determines _which_ station is valid, but can never eliminate the valid station entirely — every deficit region must be balanced by a surplus region.
- Think of it as a zero sum game -- in order for there to be an unlucky streak of gas stations that has insufficient gas, there must be a complement set of gas stations that have excess gas

---

## Approach

1. If `sum(gas) < sum(cost)`, return -1 immediately.
2. Otherwise, scan linearly with a running tank and a candidate start index.
3. At each station, add `gas[i] - cost[i]` to the running tank.
4. If the running tank goes negative, reset it to 0 and set the candidate to `i+1`.
5. Return the final candidate.

---

## Why This Works

- If we start at `candidate` and the tank goes negative at station `k`, then no station between `candidate` and `k` can be the answer either — they were all reached with a positive tank from `candidate`, meaning starting fresh at any of them would leave even less gas at station `k`. So we safely skip the whole window.

- Since a solution is guaranteed (total gas >= total cost), the last surviving candidate must be it. The global sum check serves as the verification — no second pass around the circuit is needed.

---

## Edge Cases

- Single station: valid if `gas[0] >= cost[0]`
- All stations break even (`gas[i] == cost[i]`): answer is 0
- Only the last station has surplus: answer may be 0 (surplus covers wraparound deficit)

---

## Time & Space Complexity

- Time: O(n) -- we make a single pass through the gas and cost arrays
- Space: O(1) -- we only use a few variables for tracking the candidate and running sum

---

## Common Mistakes

- Thinking a second verification pass is needed after finding the candidate — it isn't, because the global sum check already guarantees correctness. This would lead to O(n²) time complexity.

---

## Alternative Solutions

- Brute force: try each valid station (gas >= cost) as a start and simulate — O(n²).
- Prefix sum approach: find the index of the minimum prefix sum of `diff[i] = gas[i] - cost[i]`; the answer is `(min_index + 1) % n` — also O(n).
  - This works because the station after the point of minimum prefix sum is where the surplus starts to accumulate, ensuring a full circuit can be completed from there.
