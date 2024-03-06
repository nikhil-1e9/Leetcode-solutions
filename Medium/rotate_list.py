# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  """
  Given the head of a linked list, rotate the list to the right by k places.
  """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 0
        tmp = head
        last = None
        while tmp:
            last = tmp
            tmp = tmp.next
            length += 1
        
        k = k % length
        cur = head
        for _ in range(length-k-1):
            cur = cur.next
        
        start = cur.next
        last.next = head
        cur.next = None

        return start if start else head
