'''
Problem Statement ->
            You have a queue of integers, you need to retrieve the first 
            unique integer in the queue.

            Implement the FirstUnique class:

            FirstUnique(int[] nums) Initializes the object with the 
            numbers in the queue.

            int showFirstUnique() returns the value of the first unique 
            integer of the queue, and returns -1 if there is no such integer.

            void add(int value) insert value to the queue.
'''

#Solution Using Doubly Linked List : Time O(1) per operation, Space O(n)


class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
           
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = None
        self.tail = None
        self.hash = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        if self.head is None:
            return -1
        return self.head.value
    

    def add(self, value: int) -> None:
        if self.head is None and value not in self.hash:
            self.head = Node(value)
            self.tail = self.head
            self.hash[value] = self.tail
            return
        if value in self.hash:
            node = self.hash[value]
            self.nodecut(node)
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.hash[value] = self.tail
            
    def nodecut(self,node):
        if node is self.head:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            node.next = None
        if node is self.tail:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            node.prev = None
            return
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
        
    def printlist(self):
        node = self.head
        arr = []
        while node is not None:
            arr.append(node.value)
            node = node.next
        print(arr)
        
    def printheadtail(self):
        if self.head is not None:
            print(self.head.value, end = " ")
        else:
            print(None, end = " ")
        if self.tail is not None:
            print(self.tail.value)
        else:
            print(None)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)