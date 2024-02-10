# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  """
  You are given the heads of two sorted linked lists list1 and list2.

  Merge the two lists into one sorted list. 
  The list should be made by splicing together the nodes of the first two lists.

  Return the head of the merged linked list.
  """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        ans = ListNode()
        head = ans
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                ans.next = cur1
                cur1 = cur1.next
            else:
                ans.next = cur2
                cur2 = cur2.next
            ans = ans.next
        
        ans.next = cur1 or cur2
        
        return head.next
