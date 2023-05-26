#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
"""
As a reminder, backtracking is a general algorithm for finding all (or some) solutions to some computational problems. 
The idea is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack") as soon as it determines that the candidate cannot lead to a final solution.

"""
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking with counter 
        # def backtrack(comb, remain, curr, counter, results):
        #     if remain == 0:
        #         # make a deep copy of the current combination
        #         #   rather than keeping the reference.
        #         results.append(list(comb))
        #         return
        #     elif remain < 0:
        #         return

        #     for next_curr in range(curr, len(counter)):
        #         candidate, freq = counter[next_curr]

        #         if freq <= 0:
        #             continue

        #         # add a new element to the current combination
        #         comb.append(candidate)
        #         counter[next_curr] = (candidate, freq-1)

        #         # continue the exploration with the updated combination
        #         backtrack(comb, remain - candidate, next_curr, counter, results)

        #         # backtrack the changes, so that we can try another candidate
        #         counter[next_curr] = (candidate, freq)
        #         comb.pop()

        # results = []  # container to hold the final combinations
        # counter = Counter(candidates)
        # # convert the counter table to a list of (num, count) tuples
        # counter = [(c, counter[c]) for c in counter]

        # backtrack(comb = [], remain = target, curr = 0,
        #         counter = counter, results = results)

        # return results
    

    # we can also do backtracking with index, just as 90 subset ii dedup
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                if candidates[i - 1] == candidates[i] and i > start:
                    continue
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i+1)
                # backtrack, remove the number from the combination
                comb.pop()

        candidates.sort()
        backtrack(target, [], 0)

        return results
# @lc code=end

