# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        queue = deque([root])

        count = 0
        while queue:
            count += 1
            level_ans = []

            current_length = len(queue)
            for _ in range(current_length):
                node = queue.popleft()
                level_ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if (count % 2) == 0: #if count is at an even level reverse values in queue
                level_ans.reverse()
                ans.append(level_ans)
            else: #if count at odd level just append the values in queue
                ans.append(level_ans)
        
        return ans
        