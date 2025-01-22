class Solution:
    def getDistanceToClosestWaterCell(
        self, all_water_cell: list[list[int]], line_num: int, col_num: int
    ) -> int:
        distance = -1
        for water_cell in all_water_cell:
            if distance == -1:
                distance = abs(line_num - water_cell[0]) + abs(
                    col_num - water_cell[1]
                )
            elif (
                abs(line_num - water_cell[0]) + abs(col_num - water_cell[1])
                < distance
            ):
                distance = abs(line_num - water_cell[0]) + abs(
                    col_num - water_cell[1]
                )
        return distance

    def highestPeak(self, is_water: list[list[int]]) -> list[list[int]]:
        line_max = len(is_water)
        col_max = len(is_water[0])
        new_matrix = [[-1 for _ in range(col_max)] for _ in range(line_max)]
        all_water_cell = []

        for line_num in range(line_max):
            for col_num in range(col_max):
                if is_water[line_num][col_num] == 1:
                    all_water_cell.append([line_num, col_num])

        for line_num in range(line_max):
            for col_num in range(col_max):
                new_matrix[line_num][col_num] = (
                    self.getDistanceToClosestWaterCell(
                        all_water_cell, line_num, col_num
                    )
                )

        return new_matrix


teste = Solution()
print(teste.highestPeak([[0, 1], [0, 0]]))
