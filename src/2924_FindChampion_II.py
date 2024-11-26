class Solution:
    def findChampion(self, n: int, edges: list[ list[ int ] ]) -> int:
        number_of_stronger_nodes_per_n = [0] * n
        minumun_value = 1000
        index_champion = -1
        dupes = 0
        for edge in edges:
            number_of_stronger_nodes_per_n[edge[1]] += 1
        for n in range(n):
            if number_of_stronger_nodes_per_n[n] <= minumun_value:
                minumun_value = number_of_stronger_nodes_per_n[n]
                index_champion = n
        for n in number_of_stronger_nodes_per_n:
            if n == number_of_stronger_nodes_per_n[index_champion]:
                dupes += 1
        if dupes != 1:
            return -1
        return index_champion

teste = Solution()
print(teste.findChampion(n = 2, edges = [[1,0]]))
