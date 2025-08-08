# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node before head
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n+1): # +1 because we stop at node before node to be deleted
            fast = fast.next

        while fast:
            slow = slow.next 
            fast = fast.next

        #delete node
        slow.next = slow.next.next

        return dummy.next
        