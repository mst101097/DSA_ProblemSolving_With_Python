class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def reverselinklistFirst(head):

    if head is None or head.next is None:
        return head

    smallhead = reverselinklist(head.next)
    curr = smallhead

    while curr.next is not None: # time complex is O(n)2
        curr = curr.next

    curr.next = head
    head.next = None

    return smallhead


def printLinkList(head):
    if head is None:
        print("There is No data In linkList ")
    else:
        while head is not None:
            print(str(head.data)+ "->",end="")
            head = head.next
        print("None")
        return

def takeInputSecondMethod():
    inputList = [int(element) for element in input().split()]
    head = None
    tail = None # this is used for last node refreance
    for currData in inputList:

        if currData == -1: # this used for there is no data in List
            break
        newNode = Node(currData) # create node through currdata in listelement

        if head is None: # this condition used when head is none so first node create as a head
            head = newNode
            tail = newNode

        else: # after tails refrenance we dont need to traverse a linklist
            tail.next = newNode
            tail = newNode
    return head


head = takeInputSecondMethod()
printLinkList(head)
head = reverselinklist(head)
printLinkList(head)

'''
output :
1 2 3 4 5 6 -1
1->2->3->4->5->6->None
6->5->4->3->2->1->None
'''