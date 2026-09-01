# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list=[]
        while head:
            new_list.append(head.val)
            head = head.next

        new_list.reverse()
        if not new_list:
            return None

        else:

            result = ListNode(new_list[0])
            current = result

            for val in new_list[1:]:
                current.next = ListNode(val)
                current = current.next
            
            return result