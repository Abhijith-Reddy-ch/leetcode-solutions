class Solution:
    def generate_row(self,numRows: int) -> List[int]:
        ans_row = [1]
        ans = 1
        for col in range(1, numRows + 1):
            ans = ans * (numRows - col + 1)
            ans = ans // col
            ans_row.append(ans)
        return ans_row

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for col in range(numRows):
            ans.append(self.generate_row(col))
        return ans
            
    
    