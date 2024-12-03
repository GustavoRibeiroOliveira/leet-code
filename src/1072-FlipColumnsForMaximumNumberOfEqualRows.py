class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        mp = {}
        for row in matrix:
            pattern = 0
            term0 = row[0]
            for j, x in enumerate(row):
                pattern |= (x ^ term0) << j
            if pattern not in mp:
                mp[pattern] = 1
            else:
                mp[pattern] += 1
        return max(mp.values())


teste = Solution()
print(teste.maxEqualRowsAfterFlips(matrix=[[0, 1], [1, 1]]))
