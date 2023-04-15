# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head == None:
            return head
        else:
            odd = head
            even = head.next
            even_head = even
            while even != None and even.next != None:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            odd.next = even_head
            return head
        
print(Solution().oddEvenList([1,2,3,4,5]))