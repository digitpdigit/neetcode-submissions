class Solution:
    def createValidArray(self) -> List[int]:
        valid_array = [0] * 9
        return valid_array
    
    def mapVertical(self, index:int) -> Tuple(str, int):
        v_index = index % 9
        cell_index = (index - v_index) / 9
        return (f"v{v_index}", int(cell_index))
    
    def mapHorizontal(self, index:int) -> Tuple(str, int):
        h_index = math.floor(index/9)
        cell_index = index % 9
        return (f"h{h_index}", int(cell_index))

    def mapCluster(self, index: int) -> Tuple[str, int]:
        row = index // 9
        col = index % 9

        cluster_index = (row // 3) * 3 + (col // 3)
        cell_index = (row % 3) * 3 + (col % 3)

        return (f"c{cluster_index}", cell_index)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical = {f"v{i}": self.createValidArray() for i in range(9)}
        horizontal = {f"h{i}": self.createValidArray() for i in range(9)}
        cluster = {f"c{i}": self.createValidArray() for i in range(9)}

        one_clamped_array = [cell for row in board for cell in row]

        # Rules
        # vertically 0, 9, 18 is v0, 1, 10, 19 is v1
        # horizontally 0-8 is v0 9-17 is v1
        # clumped  0,1,2,9,10,11,18,19,20 c0
        for i, val in enumerate(one_clamped_array):
            (v_index, v_c_index) = self.mapVertical(i)
            (h_index, h_c_index) = self.mapHorizontal(i)
            (c_index, c_c_index) = self.mapCluster(i)

            # Now to ensure that no duplicates on each group
            if val != '.':
                int_val = int(val) - 1
                vertical[v_index][int_val] += 1
                horizontal[h_index][int_val] += 1
                cluster[c_index][int_val] += 1

                if vertical[v_index][int_val] >= 2 or horizontal[h_index][int_val] >= 2 or cluster[c_index][int_val] >= 2:
                    return False
        
        return True
        