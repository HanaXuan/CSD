class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0
    def len(self):
        return self.size
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    def enqueue(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size +=1
    def top(self):
        print(self.head.data)
        return
    def pop(self):
        print(self.head.data)
        tmp = self.head
        self.head = self.head.next
        tmp = None

queue = Queue()
queue.enqueue(1)
queue.top()
queue.pop()
queue.pop()


