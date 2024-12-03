class Solution:
    def updateDistances(self, graph, current, distances):
        newDist = distances[current] + 1

        for neighbor in graph[current]:
            if distances[neighbor] <= newDist:
                continue

            distances[neighbor] = newDist
            self.updateDistances(graph, neighbor, distances)

    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        distances = [n - 1 - i for i in range(n)]

        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i + 1].append(i)

        answer = []

        for source, target in queries:
            graph[target].append(source)
            distances[source] = min(distances[source], distances[target] + 1)
            self.updateDistances(graph, source, distances)

            answer.append(distances[0])

        return answer


teste = Solution()
print(teste.shortestDistanceAfterQueries(n=5, queries=[[2, 4], [0, 2], [0, 4]]))
