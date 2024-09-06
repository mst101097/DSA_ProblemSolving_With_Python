class ListNode:
    def  __init__(self,val=0,next = None):
        self.val = val
        self.next =  next

#createing Node from class ListNode
class Soluation:
    def MergeTwoSortedList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1.val and l2.val:
            if l1.val < l2.val:
                tail.next = l1
                l1 =  l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail =  tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next =  l2
        
        return dummy.next
