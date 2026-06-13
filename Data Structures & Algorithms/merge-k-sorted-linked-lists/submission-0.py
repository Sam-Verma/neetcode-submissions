# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None

        def merge(head1,head2):
            dummy=ListNode()
            curr=dummy

            while head1 and head2:
                if head1.val<=head2.val:
                    curr.next=head1
                    head1=head1.next
                else:
                    curr.next=head2
                    head2=head2.next
                curr=curr.next
            
            if head1:
                curr.next=head1
            
            if head2:
                curr.next=head2

            return dummy.next
        
        for i in range(1,len(lists)):
            lists[i]=merge(lists[i],lists[i-1])
        
        return lists[-1]