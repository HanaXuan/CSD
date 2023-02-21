class Node:
    def __init__(self, data):
        self.next = None
        self.pre = None
        self.data = data
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    def checkEmpty(self):
        if self.size == 0:
            return True
        return False
    def showInfo(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=' ')
            tmp=tmp.next
        print('size = ',self.size)
    def insertEmpty(self,data):
        newnode = Node(data)
        self.head = newnode
        self.last = self.head
        self.size+=1
    def delete_to_empty(self):
        self.__init__()
    def searchPosition(self,data):
        tmp = self.head
        index = 1
        while 0<=index<=self.size:
            if tmp.data == data:
                return index
            tmp = tmp.next
            index+=1
        return False
    def insertHead(self, data):
        newnode = Node(data)
        if self.checkEmpty() == True:
            self.insertEmpty(data)
            return
        newnode.next = self.head
        self.head.pre = newnode
        self.head = newnode
        self.size +=1
    def insertTail(self,data):
        newnode = Node(data)
        if self.checkEmpty() == True:
            self.insertEmpty(data)
            return
        self.last.next = newnode
        newnode.pre = self.last
        self.last = newnode
        self.size+=1
    def insertAfterData(self,data,new):
        newnode=Node(new)
        tmp = self.head
        while(tmp):
            if tmp.data == data:
                if tmp == self.last:
                    self.insertTail(new)
                    return
                newnode.next = tmp.next
                tmp.next = newnode
                newnode.pre = tmp
                newnode.next.pre = newnode
                self.size+=1
                return
            tmp=tmp.next
        print('Not available')
    def deleteHead(self):
        if self.checkEmpty() is True:
            return
        if self.head == self.last:
            self.delete_to_empty()
            return
        self.head = self.head.next
        self.head.pre = None
        self.size-=1
    def deleteTail(self):
        if self.checkEmpty() is True:
            return
        if self.head == self.last:
            self.delete_to_empty()
            return
        self.last = self.last.pre
        self.last.next = None
        self.size-=1
    def updateIndex(self,index,new):
        tmp = self.head
        ind = 1
        while tmp:
            if ind == index:
                tmp.data = new
                return
            tmp = tmp.next
            ind += 1
    def updateData(self,data,new):
        if self.searchPosition(data) == False:
            print('No available')
            return
        self.updateIndex(self.searchPosition(data),new)




dll = DoubleLinkedList()
menu = {
    0: 'Show info',
    1: 'Insert head',
    2: 'Insert tail',
    3: 'Insert after data',
    4: 'Delete head',
    5: 'Delete tail',
    6: 'Update by index',
    7: 'Update by data',
    8: 'Search position',
    10: 'Exit'
}
while True:
    for i in menu.keys():
        print(i,':',menu[i])
    choice = input('Your choice:')
    try:
        if choice == '0':
            dll.showInfo()
        if choice == '1':
            data = input('Newdata:')
            dll.insertHead(data)
        if choice == '2':
            data = input('Newdata:')
            dll.insertTail(data)
        if choice == '3':
            old = input('Data before:')
            data = input('Newdata:')
            dll.insertAfterData(old,data)
        if choice == '4':
            dll.deleteHead()
        if choice == '5':
            dll.deleteTail()
        if choice == '6':
            index = int(input('Your index:'))
            new = input('Newdata: ')
            dll.updateIndex(index,new)
        if choice == '7':
            old = input('Your old data:')
            new = input('Newdata: ')
            dll.updateData(old,new)
        if choice == '8':
            data = input('Data you want to search')
            print(dll.searchPosition(data))
        if choice == '10':
            break
    except:
        print('Your choice is not available')
        continue