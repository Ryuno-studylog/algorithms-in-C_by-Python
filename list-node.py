class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.nextval = self.head
        self.head = NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self, Removekey):

        headval = self.head

        if (headval is not None):
            if (headval.dataval == Removekey):
                self.head = headval.nextval
                headval = None
                return

        while (headval is not None):
            if headval.dataval == Removekey:
                break
            prev = headval
            headval = headval.nextval

        if (headval == None):
            return

        prev.nextval = headval.nextval

        headval = None


llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.listprint()