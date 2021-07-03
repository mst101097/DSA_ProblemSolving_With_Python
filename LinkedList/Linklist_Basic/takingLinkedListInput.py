
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLinkList(head):
    if head is None:
        print("There is No data In linkList ")
    else:
        while head is not None:
            print(str(head.data)+ "->",end="")
            head = head.next
        print("None")
        return


def takeInput():
    inputList = [int(element) for element in input().split()]
    head = None
    for currData in inputList:

        if currData == -1: # this used for there is no data in List
            break
        newNode = Node(currData) # create node through currdata in listelement
        
        if head is None: # this condition used when head is none so first node create as a head
            head = newNode

        else: #  if linklist have more node with head so we recuseively serach last node to store element
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head

head = takeInput()
printLinkList(head)


        