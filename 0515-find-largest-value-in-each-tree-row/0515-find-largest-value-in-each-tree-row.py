# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        queue = deque([root])
        while queue:
            nodes_in_current_level = len(queue)
            level_max = float("-inf")

            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_max)
        
        return ans
        