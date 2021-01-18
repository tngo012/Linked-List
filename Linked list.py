# Linked list
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = LinkedList()
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wedsnesday")

# Link first Node to second Node
list.headval.nextval = e2
# Link second Node to third Node
e2.nextval = e3

list.listprint()
