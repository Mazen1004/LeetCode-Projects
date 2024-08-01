class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        restricted_set = set(restricted)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            ans = 1  # Start with 1 because we are visiting this node
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted_set:
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        seen = {0}  # Start the DFS from node 0
        return dfs(0)