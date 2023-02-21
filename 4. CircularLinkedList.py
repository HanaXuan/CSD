import ctypes
class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.gae = age
class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class CircularLinkedList:
    def __init__(self,cap):
        self.last=None
        self.size=0
        self.capacity = capacity
    def showInfo(self):
        tmp=self.last
        if self.checkEmpty()==True:
            print('size =',self.size)
            return
        print(tmp.next.data)
        while(tmp.next!=self.last):
            tmp=tmp.next
            print(tmp.next.data)
        print('Size = ',self.size)
        return
    def checkEmpty(self):
        if self.last==None:
            return True
        return False
    def insertHead(self,data):
        newnode=Node(data)
        if self.checkEmpty()==True:
            self.last=newnode
            newnode.next=self.last
            self.size+=1
            return
        newnode.next = self.last.next
        self.last.next = newnode
        self.size+=1
    def insertLast(self,data):
        newnode=Node(data)
        if self.checkEmpty()==True:
            self.last=newnode
            newnode.next=newnode
            self.size+=1
            return
        newnode.next=self.last.next
        self.last.next=newnode
        self.last=newnode
        self.size+=1
        return
    def insertAfterData(self,data,newdata):
        newnode=Node(newdata)
        if self.checkEmpty() is True:
            print('Not available')
            return
        if self.last.data==data:
            self.insertLast(newdata)
            return
        tmp=self.last.next
        while (tmp!=self.last):
            if tmp.data==data:
                newnode.next=tmp.next
                tmp.next=newnode
                self.size+=1
                return
            tmp=tmp.next
        print('Not available')
    def insertAfterNode(self,node,newdata):
        if node>self.size or self.size==0 or node<1:
            print('Not available')
            return
        tmp=self.last.next
        tmp_index=1
        while tmp_index!=node:
            tmp=tmp.next
            tmp_index+=1
        self.insertAfterData(tmp.data,newdata)
    def deleteHead(self):
        if self.checkEmpty() is True:
            return
        if self.last.next==self.last:
            self.last=None
            self.size -= 1
            return
        self.last.next=self.last.next.next
        self.size -= 1
    def deleteLast(self):
        if self.checkEmpty() is True:
            return
        if self.last.next==self.last:
            self.last=None
            self.size -= 1
            return
        tmp=self.last
        while tmp.next!=self.last:
            tmp=tmp.next
        tmp.next=self.last.next
        self.last=tmp
        self.size -= 1
    def deleteAfterData(self,data):
        if self.checkEmpty() is True:
            return('Not available')
        if self.last.data==data:
            self.deleteHead()
            return
        tmp = self.last.next
        while (tmp != self.last):
            if tmp.data == data:
                if tmp.next==self.last:
                    self.deleteLast()
                    return
                tmp.next = tmp.next.next
                self.size -= 1
                return
            tmp = tmp.next
        print('Not available')
    def deleteAfterNode(self,node):
        if node>self.size or self.size==0 or node<0:
            print('Not available!')
            return
        tmp=self.last.next
        tmp_index=1
        while tmp_index!=node:
            tmp=tmp.next
            tmp_index+=1
        self.deleteAfterData(tmp.data)
    def update(self,oldata,newdata):
        if self.checkEmpty() is True:
            print('Not available')
            return
        tmp=self.last.next
        while(tmp!=self.last or oldata==self.last.data):
            if tmp.data==oldata:
                tmp.data=newdata
                return
            tmp=tmp.next
        print('Not available')



menu = {
    0: 'show_info',
    1: 'insert_head',
    2: 'insert_tail',
    3: 'insert_after_data',
    4: 'delete_head',
    5: 'delete_last',
    6: 'delete_after_data',
    7: 'update',
    8: 'insert_after_node',
    9: 'delete_after_node',
    10: 'exit'}
while True:
    capacity = input('Your capacity')
    try:
        cll=CircularLinkedList(int(capacity))
        break
    except:
        continue
while True:
    for i in menu.keys():
        print(i,':',menu[i])
    choice = input('Your choice: ')
    try:
        if int(choice)==0:
            cll.showInfo()
        if int(choice)==1:
            n = input('Your head_value: ')
            cll.insertHead(n)
        if int(choice)==2:
            n = input('Your tail_value: ')
            cll.insertLast(n)
        if int(choice)==3:
            data = input('After data :')
            new = input('New data :')
            cll.insertAfterData(data,new)
        if choice=='4':
            cll.deleteHead()
        if choice=='5':
            cll.deleteLast()
        if int(choice)==6:
            data = input('After data :')
            cll.deleteAfterData(data)
        if int(choice)==7:
            data = input('Old data :')
            new = input('New data :')
            cll.update(data,new)
        if int(choice)==8:
            data = int(input('Index count from 1, add data after index :'))
            new = input('New data :')
            cll.insertAfterNode(data,new)
        if int(choice)==9:
            data = int(input('Index count from 1, delete data after index :'))
            cll.deleteAfterNode(data)
        if int(choice)==10:
            print('You have exited')
            exit()
    except:
        print('Your choice is not available')
        continue