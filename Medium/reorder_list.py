# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  """
  You are given the head of a singly linked-list. The list can be represented as:

  L0 → L1 → … → Ln - 1 → Ln
  Reorder the list to be on the following form:
  
  L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
  You may not modify the values in the list's nodes. 
  Only nodes themselves may be changed.
  """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # i)   Find middle of list
        # ii)  Create two separate lists one upto mid and one reversed from end to mid
        # iii) Merge the two lists 
      
        ## Inital list:             1 -> 2 -> 3 -> 4 -> 5 -> None
        
        ## first list:              1 -> 2 -> 3 -> None
        
        ## second list:             4 -> 5 -> None
        
        ## Reverse second list:     5 -> 4 -> None
        
        ## Merge both lists:        1 -> 5 -> 2 -> 4 -> 3 -> None

        # Find middle node
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Break the link between the lists
        rev = slow.next
        slow.next = None

        # Reverse the rev list
        curr = rev
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Merge the 2 lists together
        h1, h2 = head, prev
        temp = head
        i = 0
        while h1 and h2:
            if i % 2 == 0:
                temp = h1.next
                h1.next = h2
                h1 = temp
            else:
                temp = h2.next
                h2.next = h1
                h2 = temp
            
            i += 1

        return head
