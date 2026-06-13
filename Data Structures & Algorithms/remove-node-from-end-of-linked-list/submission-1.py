# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        
        front=count-n

        if front==0:
            return head.next
        
        node=head
        pos=1
        while node and front!=pos:
            node=node.next
            pos+=1
        
        node.next=node.next.next

        return head

