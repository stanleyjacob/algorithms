class Solution:
    
    def climbStairsHelper(self, n: int, cache = {}) -> int:
        if n in cache:
            return cache[n]
        if n == 0:
            num_steps = 1
        elif n == 1:
            num_steps = 1
        else:
            num_steps = self.climbStairsHelper(n - 1, cache) + self.climbStairsHelper(n - 2, cache)
        cache[n] = num_steps
        return num_steps
        
    def climbStairs(self, n: int) -> int:
        return self.climbStairsHelper(n, cache = {})
