class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(current_node):
            if current_node == destination:
                return True

            if not seen[current_node]:
                seen[current_node] = True
                for next_node in graph[current_node]:
                    if dfs(next_node):
                        return True
            return False
        
        return dfs(source)
        