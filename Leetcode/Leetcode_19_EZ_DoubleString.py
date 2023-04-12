head = [1,2,3,4,5]
n = 2
class Solution:
    def removeNthFromEnd(self,head,n):
        left = head
        right = head
        for i in range(n):
            right = right.next
        if not right:
            return left.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head
    
print(Solution().removeNthFromEnd(head,n))