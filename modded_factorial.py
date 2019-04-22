
class Solution:
    
    def modded_helper(self, N):
        if N == 0:
            return 1
        
        op_arr = ['m', 'd', 'a', 's']
        curr_num = N
        i = 0
        queue_left = []
        while N > 1:
            
            if op_arr[i] == 'm':
                curr_num *= (N - 1)
                
            elif op_arr[i] == 'd':
                curr_num //= (N - 1)
                if len(queue_left) == 1:
                    curr_num = queue_left.pop() - curr_num
                
            elif op_arr[i] == 'a':
                curr_num += (N - 1)
            
            elif op_arr[i] == 's':
                queue_left.append(curr_num)
                curr_num = N - 1
                
            i += 1
            if i % 4 == 0:
                i = 0
            N -= 1
        
        if len(queue_left) == 1:
            curr_num = queue_left.pop() - curr_num
            
        return curr_num
            
    def modded(self, N: int) -> int:
        return self.modded_helper(N)
        
        
class TestClass:
    
    def modded_helper(self, N, cache = {}):
        if N == 0:
            return 1
        
        if N in cache:
            return cache[N]
        
        op_arr = ['m', 'd', 'a', 's']
        curr_num = N
        i = 0
        while N > 1:
            
            if op_arr[i] == 'm':
                curr_num *= (N - 1)
                
            elif op_arr[i] == 'd':
                curr_num //= (N - 1)
                
            elif op_arr[i] == 'a':
                curr_num += (N - 1)
            
            elif op_arr[i] == 's':
                curr_num -= self.modded_helper(N - 1, cache)
                break
                
            i += 1
            if i % 4 == 0:
                i = 0
            N -= 1
            
        return curr_num
            
    def modded(self, N: int) -> int:
        return self.modded_helper(N)
        
