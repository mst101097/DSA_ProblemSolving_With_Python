# defination of single linklist
class ListNode:
    def __init__(self, val = 0, next = None):
        self.value  = val
        self.next = next

# iterative Approche
class Soluation:
    def reverseLinklist(self, head: ListNode) -> ListNode:
        
        prev , curr = None , head
        # T O(n), M O(1)
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
# Recursive Approch
class Soluation:
    def reverseLinklist(self, head: ListNode) -> ListNode:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead =  self.reverseLinklist(head.next)
            head.next.next  = head
        head.next = None

        return newHead
        