# In this file we have create Node and create Refrance to Node in basic manner

# this is the node class which is used for create a node with two partition Node_data and NextNode_Address
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

a = Node(24)
b = Node(26)
a.next = b
print('Node a data: ',a.data)
print('Node a.next address:',a.next)
print('Node b data : ',b.data)
print('Node b next address data : ',b.next)
print('Node a next Node data : ',a.next.data)

