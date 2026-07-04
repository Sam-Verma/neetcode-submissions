"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy=Node(0)
        oldtonew={}
        curr=head
        while curr:
            copy=Node(curr.val)
            if dummy.next==None:
                dummy.next=copy
            oldtonew[curr]=copy
            curr=curr.next

        while head:
            
            copy=oldtonew[head]
            if head.next in oldtonew:
                copy.next = oldtonew[head.next]
            if head.random in oldtonew:
                copy.random = oldtonew[head.random]
            
            head=head.next
        
        return dummy.next