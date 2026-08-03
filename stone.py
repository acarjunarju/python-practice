from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0

            best = float('-inf')
            curr = 0
            for k in range(3):
                if i + k < n:
                    curr += stoneValue[i + k]
                    best = max(best, curr - dfs(i + k + 1))
            return best

        diff = dfs(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        return "Tie"
