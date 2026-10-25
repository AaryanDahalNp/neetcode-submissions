# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            head = list1
            current = list1
            another = list2
        else:
            head = list2
            current = list2
            another = list1
        
        while True:
            if not current.next:
                current.next = another
                break

            if not another:
                break

            if current.next.val > another.val:
                nxt = current.next
                current.next = another
                another = nxt
            
            current = current.next
        
        return head

        