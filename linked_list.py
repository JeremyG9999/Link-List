class Node:  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        return newnode
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = newnode
        return newnode
    def insertAfter(self, previousNode, data):
        if previousNode is None:
            print("The given previous node must be in the list.")
            return
        else:
            newnode = Node(data)
            newnode.next = previousNode.next  
            previousNode.next = newnode
def main():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.push(8)
    linked_list.insertAfter(linked_list.head.next, 6)
    print("Linked List:")
    linked_list.printList()
main()