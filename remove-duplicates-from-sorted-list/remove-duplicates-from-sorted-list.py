# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        while dummy and dummy.next: #traverses singly linked list
            if dummy.val == dummy.next.val: #checks for duplicates
                dummy.next= dummy.next.next #Deletes duplicate node
            else:
                dummy = dummy.next
            
        
        return head