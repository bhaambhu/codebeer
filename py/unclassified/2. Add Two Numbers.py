from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  def __str__(self) -> str:
    ptr = self
    s = "[ "
    while ptr is not None:
      s += str(ptr.val)+", "
      ptr = ptr.next
    s += " ]"
    return s
  
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = Optional[ListNode]
    carry = 0
    if l1 or l2:
      sum = l1.val + l2.val
      if sum > 9:
        carry = 1
        sum = sum - 10
      result = ListNode(val=sum)
      l1 = l1.next
      l2 = l2.next

    while l1 or l2:
      sum = l1.val + l2.val + carry
      carry = 0
      if sum > 9:
        carry = 1
        sum = sum-10
      result.next = ListNode(sum)
      l1 = l1.next
      l2 = l2.next
    return result.__str__()

s = Solution()
l1 = ListNode(1, ListNode(1, ListNode(1)))
l2 = ListNode(2, ListNode(2, ListNode(2)))
print(s.addTwoNumbers(l1=l1, l2=l2))