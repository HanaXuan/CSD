#add, delete (head,tail,after-before(data,node))
#update (delete, insert)
#show info, search
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def showInfo(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next
        print('size = ',self.size)
    def search(self,data):
        tmp=self.head
        while (tmp):
            if tmp.data==data:
                return tmp
            tmp=tmp.next
        return False
    def checkEmpty(self):
        if self.head==None:
            return True
        return False
    def checkNode(self,node):
        if node>self.size:
            return False
        return True
    def insertFirst(self,data):
        newnode=Node(data)
        if self.checkEmpty() == True:
            self.head=newnode
            self.size+=1
            return
        newnode.next=self.head
        self.head=newnode
        self.size+=1
    def insertTail(self,data):
        newnode = Node(data)
        tmp = self.head
        if self.checkEmpty() == True:
            self.head = newnode
            size += 1
            return
        while (tmp.next):
            tmp = tmp.next
        tmp.next = newnode
        self.size += 1
        return
    def insertAfterData(self,data,newdata):
        newnode=Node(newdata)
        tmp = self.search(data)
        if tmp == False:
            print('Error data')
            return
        newnode.next=tmp.next
        tmp.next=newnode
        self.size+=1
    def insertBeforData(self,data,newdata):
        newnode = Node(newdata)
        if self.checkEmpty() == True: #case rỗng
            print('Empty list')
            return
        tmp = self.head
        if tmp.data==data:
            newnode.next=tmp
            self.head=newnode
            self.size+=1
            return
        while (tmp.next):
            if tmp.next.data == data :
                break
            tmp = tmp.next
        if tmp.next == None or tmp.next.data!=data: #case không tìm ra data
            print('Error data')
            return
        newnode.next=tmp.next
        tmp.next=newnode
        self.size+=1
        return
    def insertAfterNode(self,node,newdata):
        newnode=Node(newdata)
        if self.checkNode(node) == False or node<1:
            print ('Error')
            return
        tmp=self.head
        tmp_index=1
        while(tmp_index!=node):
            tmp=tmp.next
            tmp_index+=1
        newnode.next=tmp.next
        tmp.next=newnode
    def insertBeforeNode(self,node,newdata):
        newnode=Node(newdata)
        if self.checkNode(node)==False:
            print('Error')
            return
        if node==1:
            newnode.next=self.head
            self.head=newnode
            self.size+=1
            return
        tmp_index=2
        tmp=self.head
        while tmp_index!=node:
            tmp=tmp.next
            tmp_index+=1
        newnode.next=tmp.next
        tmp.next=newnode
    def deleteHead(self):
        if self.checkEmpty() is True:
            return
        self.head=self.head.next
        self.size-=1
    def deleteTail(self):
        if self.checkEmpty() is True:
            return
        if self.size==1:
            self.head=None
            self.size-=1
            return
        tmp=self.head
        while tmp.next.next:
            tmp=tmp.next
        tmp.next=None
        self.size-=1
    def deleteAfterData(self,data):
        if self.search(data) is False:
            print('Error')
            return
        tmp = self.search(data)
        if tmp.next is None:
            print('Your data is the last one')
            return
        tmp.next=tmp.next.next
        self.size-=1
    def deleteBeforeData(self,data):
        if self.head.data==data:
            print('Your data is the first one')
            return
        if self.head.next.data==data:
            self.head=self.head.next
            self.size-=1
            return
        tmp = self.head
        while True:
            if tmp.next.next == None:
                print('Error')
                return
            if tmp.next.next.data==data:
                tmp.next = tmp.next.next
                self.size-=1
                return
            tmp=tmp.next
    def deleteAfterNode(self,node):
        if self.checkNode(node) is False or node<1:
            print('Error')
            return
        if node==self.size:
            print('Your Node is the last one')
            return
        tmp=self.head
        tmp_index=1
        while tmp:
            if tmp_index==node:
                tmp.next=tmp.next.next
                self.size-=1
                return
            tmp=tmp.next
            tmp_index+=1
    def deleteBeforNode(self,node):
        if node==1:
            print('Your node is the first one')
            return
        if self.checkNode(node) is False or node<1:
            print('Error')
            return
        if node==2:
            self.head=self.head.next
            self.size-=1
            return
        tmp = self.head
        tmp_index = 3
        while True:
            if tmp_index == node:
                tmp.next = tmp.next.next
                self.size -= 1
                return
            tmp = tmp.next
            tmp_index+=1
    def update(self, data,newdata):
        if self.search(data) is False:
            print('Error')
            return
        tmp=self.search(data)
        tmp.data=newdata


list=LinkedList()

menu = {
    1: 'insert',
    2: 'delete',
    3: 'search',
    4: 'update',
    4: 'show info',
    5: 'exit'
}

while True:
    print(menu)
    choice = int(input())
    if 
list.insertFirst(2)
list.insertAfterData(2,0)
list.insertBeforData(0,10)
list.insertAfterNode(-1,30)
list.insertBeforeNode(4,20)
list.insertTail(3)
#list.deleteHead()
#list.deleteTail()
#list.deleteAfterData(999)
#list.deleteBeforeData(8)
list.deleteAfterNode(4)
list.deleteBeforNode(3)
list.update(0,100)
list.showInfo()
