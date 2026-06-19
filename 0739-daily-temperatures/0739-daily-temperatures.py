from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        
        # Loop backwards from the second-to-last day to the first day
        for i in range(n - 2, -1, -1):
            j = i + 1
            
            # Instead of j += 1, we "jump" using the result array
            while j < n and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    j = n  # No warmer day exists ahead, break out
                else:
                    j += result[j]  # Jump directly to the next warmer day
            
            # If we found a valid warmer day within bounds
            if j < n:
                result[i] = j - i
                
        return result
