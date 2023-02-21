#insert, remove (thông qua giá trị, vị trí), add
import ctypes
from random import randint
class array:
    def __init__(self):
        self.capacity=1
        self.data=self.create(self.capacity)
        self.s=0
    def create(self,capacity):
        return(capacity * ctypes.py_object)()
    def info(self):
        print('Actual number:',self.s)
        print('Capacity',self.capacity)
        for i in range(self.s):
            print('Element',i,':',self.data[i])
    def len(self):
        return self.capacity
    def check_full(self):
        if self.s==self.capacity:
            return True
    def getitem(self,i):
        if 0<=i<=self.s:
            return self.data[i]
        return print('False index')
    def resize(self,newsize):
        newarray = self.create(newsize)
        for i in range(self.s):
            newarray[i]=self.data[i]
        self.data=newarray
        self.capacity=newsize
    def append(self,data):
        if self.check_full() is True:
            self.resize(2 * self.capacity)
        self.data[self.s]=data
        self.s+=1
    def insert(self,index,data):
        if self.check_full() is True:
            self.resize(2 * self.capacity)
        for i in range(self.s,index,-1):
            self.data[i]=self.data[i-1]
        self.data[index]=data
        self.s+=1
    def remove_data(self,data):
        for i in range(self.s):
            if self.data[i]==data:
                for j in range(i,self.s-1):
                    self.data[j]=self.data[j+1]
                self.data[self.s]=0
                self.s-=1
                return
    def remove_index(self,index):
        for i in range(self.s):
            if i==index:
                for j in range(i,self.s):
                    self.data[j]=self.data[j+1]
                self.data[self.s]=0
                self.s-=1
                return
        print('False index')
a = array()
a.create(3)
a.append(2)
a.append(5)
a.insert(1,0)
a.remove_data(0)
a.remove_index(0)
a.info()
