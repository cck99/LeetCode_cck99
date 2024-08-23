class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        current_rows = [''] * numRows
        rows = 0
        control = False
        
        for char in s:
            current_rows[rows] += char
            
            if rows == 0 or rows == numRows - 1:
                control = not control
            

            rows += 1 if control else -1

            print(f"After update: rows={rows}")
        
        return ''.join(current_rows)
