class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      # Iterate through each row in the matrix
        for row in matrix:
            # If the last element of the row is >= target,
            # then the target could be in this row
            if row[-1] >= target:
                # Scan through the row to check for the target
                for col in row:
                    if col == target:
                        return True  # Target found
        # Target was not found in any row
        return False