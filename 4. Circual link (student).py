class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def showStudent(self):
        print('Id of student: ', self.id)
        print('name of student: ', self.name)
        print('age of student: ', self.age)
    def set_id(self,id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_age(self,age):
        self.age = age
class CircularLinkedList:
    class Node:
        def __init__(self,data):
            self.next = None
            self.data = data
    def __init__(self):
        self.last=None
        self.size=0
    def showInfo(self):
        a = 1
        tmp=self.last
        if self.checkEmpty()==True:
            print('size =',self.size)
            return
        print('Student ',a,'----------')
        a+=1
        tmp.next.data.showStudent()
        while(tmp.next!=self.last):
            tmp=tmp.next
            print('Student ', a, '----------')
            a += 1
            tmp.next.data.showStudent()
        print('Total student = ',self.size)
        return
    def check_id(self,idd):
        if self.last.data.id == idd:
            return True
        tmp = self.last.next
        if tmp.data.id == idd:
            return True
        while tmp!= self.last:
            tmp = tmp.next
            if tmp.data.id == idd:
                return True
        return False
    def insertLast(self,data):
        newnode=self.Node(data)
        if self.checkEmpty()==True:
            self.last=newnode
            newnode.next=newnode
            self.size+=1
            return
        if self.check_id(newnode.data.id):
            print('Existed')
            return
        newnode.next=self.last.next
        self.last.next=newnode
        self.last=newnode
        self.size+=1
        return
    def checkEmpty(self):
        if self.last==None:
            return True
        return False
    def update(self,oldata,id,name,age):
        tmp=self.last.next
        while(tmp.data.id!=self.last.data.id or oldata==self.last.data.id):
            if tmp.data.id==oldata:
                tmp.data.set_id(id)
                tmp.data.set_name(name)
                tmp.data.set_age(age)
                return
            tmp=tmp.next
        print('Not available')
    def delete_id (self,id):
        if self.last.data.id==id:
            if self.last.next == self.last:
                self.last = None
                self.size -= 1
                print('Deleted!')
                return
            self.last.next = self.last.next.next
            self.size -= 1
            print('Deleted!')
            return
        tmp = self.last.next
        while (tmp != self.last):
            if tmp.data.id == data.id:
                if tmp.next==self.last:
                    if self.last.next == self.last:
                        self.last = None
                        self.size -= 1
                        print('Deleted!')
                        return
                    tmp = self.last
                    while tmp.next != self.last:
                        tmp = tmp.next
                    tmp.next = self.last.next
                    self.last = tmp
                    self.size -= 1
                    print('Deleted!')
                    return
                tmp.next = tmp.next.next
                self.size -= 1
                print('Deleted!')
                return
            tmp = tmp.next
        print('Not found your id')
    def search(self,name):
        a = 1
        tmp = self.last.next
        if self.size == 1:
            if self.last.data.name == name:
                self.last.data.showStudent()
                return
        while tmp!=self.last:
            if tmp.data.name == name:
                print(a,':------------')
                tmp.data.showStudent()
                a+=1
            tmp = tmp.next
        if self.last.data.name == name:
            print(a, ':------------')
            self.last.data.showStudent()




menu = {
    0: 'display',
    1: 'insert_last_list',
    2: 'delete_by_id',
    3: 'update',
    4: 'search',
    5: 'exit'}
cll=CircularLinkedList()
while True:
    print('----------------------------------------------')
    for i in menu.keys():
        print(i,':',menu[i])
    choice = input('Your choice: ')
    try:
        if int(choice)==0:
            cll.showInfo()
        if int(choice)==1:
            id = input('New id:')
            name = input('New name:')
            age = input('New age:')
            new_student = Student(id, name, age)
            cll.insertLast(new_student)
        if choice=='2':
            if cll.checkEmpty():
                print('Your list is empty')
                continue
            id = input('Your id:')
            cll.delete_id(id)
        if int(choice)==3:
            if cll.checkEmpty():
                print('Your list is empty')
                continue
            data = input('Old id :')
            id = input('New id :')
            name = input('New name')
            age = input('New age:')
            cll.update(data,id,name,age)
        if int(choice)==5:
            print('You have exited')
            break
        if int(choice) == 4:
            if cll.checkEmpty():
                print('Your list is empty')
                continue
            name = input('Your name')
            cll.search(name)
    except:
        print('Your choice is not available')
        continue