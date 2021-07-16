
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


def lengthOfLinklist(head):
    count = 0
    while head is not None:
        count = count+1
        head = head.next
    return count


# Print ith node in Linklist

def printIthNode(head,i):
    curr = head
    counter = 0

    while counter<i and curr != None:
            curr = curr.next
            counter = counter + 1

    print(curr.data)



def insertAtIR(head,i,data):
    # recursivly insert element in linklist in Ith Position 

    if i<0:
        return head
    
    if i==0:
        newNode =  Node(data)
        newNode.next = head
        return newNode

    if head is None:
        return None
    smallhead = insertAtIR(head.next,i-1,data)
    head.next = smallhead
    return head

def insertAtI(head,i,data):

    # this is itratively approch to insert an element in linklist Ith position 

    if i<0 or i>lengthOfLinklist(head):
        return head

    count = 0
    prev = None
    curr = head

    while count<i:
        prev = curr
        curr = curr.next
        count = count+1

    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr

    return head


# this method used for delete a node with  given value
def deleteANode(head,val):

    # condition 1 if head is empty
    if head is None:
        print('Linklist is Empty !')

    # condition 2 if delete value is head value
    if head.data == val:
        head = head.next

    # than given value if node head value but have in mid in linklist
    temp = head
    while temp.next is not None:

        if temp.data ==val:
            break
        temp = temp.next

    if temp.next is None:
        print('Node is not find in Linklist !')

    else:
        temp.next = temp.next.next





# first method to take input
# def takeInput():
#     inputList = [int(element) for element in input().split()]
#     head = None
#     for currData in inputList:

#         if currData == -1: # this used for there is no data in List
#             break
#         newNode = Node(currData) # create node through currdata in listelement
        
#         if head is None: # this condition used when head is none so first node create as a head
#             head = newNode

#         else: #  if linklist have more node with head so we recuseively serach last node to store element
#             curr = head
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = newNode
#     return head

# head = takeInput()
# printLinkList(head)

#( Second Method to take input through optimize way )
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
insertAtIR(head,2,9)
printLinkList(head)
insertAtIR(head,0,10)
printLinkList(head)
printIthNode(head,2)
deleteANode(head,3)
printLinkList(head)



