class Node:
    def __init__(self, data):
         self.data = data 
         self.next = None
class LinkedList: 
    def __init__(self):
        self.start = None
    def push(self, value):
         new_node = Node(value)
         new_node.next = self.start
         self.start = new_node 
    def printMiddle(self):
         slow_ptr = self.start
         fast_ptr = self.start
         if self.start is not None:
               while (fast_ptr is not None and fast_ptr.next is not None):
                    fast_ptr = fast_ptr.next.next
                    slow_ptr = slow_ptr.next
               print("The middle element is: ", slow_ptr.data)
list1 = LinkedList()
list1.push(5)
list1.push(9) 
list1.push(12)
list1.push(20) 
list1.push(3) 
list1.push(14) 
list1.printMiddle()